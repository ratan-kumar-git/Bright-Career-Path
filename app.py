from flask import Flask, render_template, url_for, session, redirect, flash, request
from flask_sqlalchemy import SQLAlchemy
import bcrypt
from werkzeug.utils import secure_filename
import os
import re


app = Flask(__name__)

# DB Connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///services.db'
db = SQLAlchemy(app)

app.secret_key = 'Bablu@12345'

# Configuration
app.config['UPLOAD_FOLDER'] = 'static/images'
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024  # 5MB max size

def allowed_file(filename):
    allowed_extensions = {'png', 'jpg', 'jpeg'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

def slugify(text):
    text = text.strip().lower().replace(' ', '_')
    return re.sub(r'[^a-z_]', '', text)


# Admin Table
class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __init__(self, email, password, name):
        self.name = name
        self.email = email
        self.password = self.hash_password(password)
        
    def hash_password(self, password):
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def check_password(self, password):
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))

# Services Table
class Service(db.Model):
    url = db.Column(db.String(100), primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    short_description = db.Column(db.String(255), nullable=False)
    img_filename = db.Column(db.String(100), nullable=False)

    descriptions = db.relationship('ServiceDescription', backref='service', lazy=True, cascade="all, delete")

# Sevices Details Table
class ServiceDescription(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service_url = db.Column(db.String(100), db.ForeignKey('service.url'), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)

    images = db.relationship('ServiceImage', backref='description', lazy=True, cascade="all, delete")
    videos = db.relationship('ServiceVideo', backref='description', lazy=True, cascade="all, delete")

# multiple images per description
class ServiceImage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description_id = db.Column(db.Integer, db.ForeignKey('service_description.id'), nullable=False)
    img_filename = db.Column(db.String(255), nullable=False)

# multiple YouTube links per description
class ServiceVideo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description_id = db.Column(db.Integer, db.ForeignKey('service_description.id'), nullable=False)
    yt_embed_link = db.Column(db.String(500), nullable=False)

# Contact Us Table
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    number = db.Column(db.String(100), nullable=False)
    message = db.Column(db.String(500), nullable=False)

with app.app_context():
    db.create_all()


# Home Page
@app.route('/')
def index():
    services = Service.query.all() 
    return render_template('home.html', title='Home | Bright Career Path', services=services, len=len)


# Services Page
@app.route('/services')
def services():
    services = Service.query.all() 
    return render_template('services.html', title='Our Services', services=services, len=len)


# Services_page Page
@app.route('/services/<name>')
def services_page(name):
    services_page_data = ServiceDescription.query.filter_by(service_url=name).first()
    if not services_page_data:
        return render_template('error.html'), 404

    services_page_img = ServiceImage.query.filter_by(description_id=services_page_data.id).all()
    services_page_video = ServiceVideo.query.filter_by(description_id=services_page_data.id).all()

    return render_template(
        'services_page.html', 
        title=f'{services_page_data.title} | Service', 
        services_page_data = services_page_data,
        services_page_img=services_page_img,
        services_page_video=services_page_video,
        len= len, 
        )


# About Page
@app.route('/about')
def about():
    return render_template('about.html', title='About')


# Contact Page
@app.route('/contact', methods=['POST','GET'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        number = request.form['number']
        message = request.form['message']

        new_data = Contact(name=name, email=email, number=number, message=message)
        db.session.add(new_data)
        db.session.commit()    
        flash('Message Send Successful.', 'success')
    return render_template('contact.html', title='Contact')


# Policy Page
@app.route('/policy')
def policy():
    return render_template('policy.html', title='Policy')

# Admin Login
@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = Admin.query.filter_by(email=email).first()
        if user and user.check_password(password):
            session['admin_id'] = user.id
            return redirect(url_for('admin_dashboard'))
        else:
            flash("Invalid Credentials", "danger")
    return render_template('admin/admin_login.html', title='Admin Login')

# Admin Logout
@app.route('/admin/logout')
def admin_logout():
    session.pop('admin_id', None)
    return redirect(url_for('admin_login'))

# Admin Dashboard + Shows all Services
@app.route('/admin', methods=['GET', 'POST'])
def admin_dashboard():
    if 'admin_id' not in session:
        return redirect(url_for('admin_login'))

    if request.method == 'POST':
        title = request.form['title']
        url = slugify(title)
        short_description = request.form['short_description']
        img_file = request.files.get('img_filename')

        # Validation
        errors = []
        if not title or len(title) > 100:
            errors.append("Title is required and must be under 100 characters.")
        if not url or not url.isidentifier():  # letters, numbers, underscores
            errors.append("URL must contain only letters, digits, and underscores.")
        if not img_file or not allowed_file(img_file.filename):
            errors.append("Valid image file required (jpg, jpeg, png, etc).")
        if not short_description or len(short_description) > 500:
            errors.append("Description is required and must be under 500 characters.")
        

        if errors:
            for err in errors:
                flash(err, "danger")
            return redirect(url_for('admin_dashboard'))

        # Handle image saving
        filename = secure_filename(img_file.filename)
        save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

        # Avoid overwriting
        base, ext = os.path.splitext(filename)
        count = 1
        while os.path.exists(save_path):
            filename = f"{base}_{count}{ext}"
            save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            count += 1

        try:
            img_file.save(save_path)  # ✅ Save image first
            new_service = Service(
                url=url,
                title=title,
                short_description=short_description,
                img_filename=filename
            )
            new_service_describe = ServiceDescription(
                service_url=url,
                title=title,
                description=short_description
            )
            db.session.add(new_service)
            db.session.add(new_service_describe)
            db.session.commit()
            flash("Service added successfully.", "success")

        except Exception as e:
            os.remove(save_path)
            db.session.rollback()
            flash(f"Failed to save service: {str(e)}", "danger")

        return redirect(url_for('admin_dashboard'))


    services = Service.query.all()
    contacts = Contact.query.all()
    return render_template('admin/admin.html', title='Admin Dashboard', services=services, contacts=contacts)

# Deleting Services
@app.route('/admin/delete/<url>', methods=['POST'])
def delete_service(url):
    if 'admin_id' not in session:
        return redirect(url_for('admin_login'))

    try:
        service = Service.query.filter_by(url=url).first_or_404()
        service_data = ServiceDescription.query.filter_by(service_url=service.url).first()
        img_service_data = ServiceImage.query.filter_by(description_id=service_data.id).all()

        # Services Image
        img_filename = service.img_filename
        delete_path = os.path.join(app.config['UPLOAD_FOLDER'], img_filename)

        db.session.delete(service)
        db.session.commit()

        if delete_path and os.path.exists(delete_path):
            try:
                # All Images inside service
                inside_img_filename = []
                if img_service_data:
                    for img_file in img_service_data:
                        delete_inside_path = os.path.join(app.config['UPLOAD_FOLDER'], img_file.img_filename)
                        inside_img_filename.append(delete_inside_path)

                    if delete_inside_path and os.path.exists(delete_inside_path):
                        for inside_path in inside_img_filename:
                            os.remove(inside_path)
                os.remove(delete_path)
            except Exception as file_error:
                flash(f"Service deleted, but image file couldn't be removed: {file_error}", "warning")

        flash("Service deleted successfully.", "success")

    except Exception as e:
        db.session.rollback()
        flash(f"Error deleting service: {str(e)}", "danger")

    return redirect(url_for('admin_dashboard'))

# Editing Services
@app.route('/admin/edit/<url>', methods=['GET', 'POST'])
def edit_service(url):
    if 'admin_id' not in session:
        return redirect(url_for('admin_login'))

    service = Service.query.filter_by(url=url).first()
    
    if request.method == 'POST':
        # if image not send then run this 
        if not request.files.get('img_filename'):
            service.title = request.form['title']
            service.short_description = request.form['short_description']

            db.session.commit()
            flash("Service updated successfully.", "success")
            return redirect(url_for('admin_dashboard'))
        

        # when image found then run this
        title = request.form['title']
        short_description = request.form['short_description']
        img_file = request.files.get('img_filename')

        # Validation
        errors = []
        if not title or len(title) > 100:
            errors.append("Title is required and must be under 100 characters.")
        if not img_file or not allowed_file(img_file.filename):
            errors.append("Valid image file required (jpg, jpeg, png, etc).")
        if not short_description or len(short_description) > 500:
            errors.append("Description is required and must be under 500 characters.")

        if errors:
            for err in errors:
                flash(err, "danger")
            return redirect(request.referrer or url_for('admin_dashboard'))

        # Handle image saving
        filename = secure_filename(img_file.filename)
        save_img_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        delete_img_path = os.path.join(app.config['UPLOAD_FOLDER'], service.img_filename)

        # Avoid overwriting
        base, ext = os.path.splitext(filename)
        count = 1
        while os.path.exists(save_img_path):
            filename = f"{base}_{count}{ext}"
            save_img_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            count += 1

        try:
            img_file.save(save_img_path) #save new img

            #delete old img if save new img
            if os.path.exists(delete_img_path):
                os.remove(delete_img_path) 

            # Update database
            service.title = title
            service.short_description = short_description
            service.img_filename = filename
            db.session.commit()
            flash("Service Update successfully.", "success")

        except Exception as e:
            if os.path.exists(save_img_path):
                os.remove(save_img_path)
            db.session.rollback()
            flash(f"Failed to Update service: {str(e)}", "danger")


    return render_template('admin/edit_service.html', title='Edit Service', service=service)

# Show content of Service Page
@app.route('/admin/<service_url>', methods=['GET', 'POST'])
def admin_service_data(service_url):
    if 'admin_id' not in session:
        return redirect(url_for('admin_login'))
    service_data = ServiceDescription.query.filter_by(service_url=service_url).first()
    img_service_data = ServiceImage.query.filter_by(description_id=service_data.id).all()
    video_service_data = ServiceVideo.query.filter_by(description_id=service_data.id).all()

    return render_template('admin/admin_services.html', title='Service Data | Admin', service_data=service_data, img_service_data=img_service_data, video_service_data=video_service_data, len=len)

# Update Title & Description of services
@app.route('/admin/update_desc_service/<url>', methods=['POST'])
def update_desc_service(url):
    if 'admin_id' not in session:
        return redirect(url_for('admin_login'))
    
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']

    try:
        update_desc_service = ServiceDescription.query.filter_by(service_url=url).first()
        update_desc_service.title=title
        update_desc_service.description=description

        db.session.commit()
        flash("Title & Description update successfully.", "success")

    except Exception as e:
        db.session.rollback()
        flash(f"Failed to save Title & Description: {str(e)}", "danger")

    return redirect(request.referrer or url_for('admin_dashboard'))

# Upload Services Images
@app.route('/admin/upload_img_service/<description_id>', methods=['POST'])
def upload_img_service(description_id):
    if 'admin_id' not in session:
        return redirect(url_for('admin_login'))
    
    if request.method == 'POST':
        img_file = request.files.get('img_filename')

    if not img_file or not allowed_file(img_file.filename):
        flash("Valid image file required (jpg, jpeg, png, etc).", "danger")
        return redirect(request.referrer or url_for('admin_dashboard'))
        
    # Handle image saving
    filename = secure_filename(img_file.filename)
    save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

    # Avoid overwriting
    base, ext = os.path.splitext(filename)
    count = 1
    while os.path.exists(save_path):
        filename = f"{base}_{count}{ext}"
        save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        count += 1

    try:
        img_file.save(save_path)
        
        new_image = ServiceImage(description_id=description_id, img_filename=filename)
        db.session.add(new_image)
        db.session.commit()
        flash("Image upload successfully.", "success")

    except Exception as e:
        os.remove(save_path)
        db.session.rollback()
        flash(f"Failed to save Image: {str(e)}", "danger")

    return redirect(request.referrer or url_for('admin_dashboard'))

# Deleting Service Imgages 
@app.route('/admin/delete_img_service/<id>', methods=['POST'])
def delete_img_service(id):
    if 'admin_id' not in session:
        return redirect(url_for('admin_login'))

    try:
        img_service_data = ServiceImage.query.filter_by(id=id).first()
        img_filename = img_service_data.img_filename
        delete_path = os.path.join(app.config['UPLOAD_FOLDER'], img_filename)

        db.session.delete(img_service_data)
        db.session.commit()

        if delete_path and os.path.exists(delete_path):
            try:
                os.remove(delete_path)
            except Exception as file_error:
                flash(f"Image path deleted, but image file couldn't be removed: {file_error}", "warning")

        flash("Image deleted successfully.", "success")

    except Exception as e:
        db.session.rollback()
        flash(f"Error deleting service: {str(e)}", "danger")

    return redirect(request.referrer or url_for('admin_dashboard'))

# Upload Services Video
@app.route('/admin/upload_video_service/<description_id>', methods=['POST'])
def upload_video_service(description_id):
    if 'admin_id' not in session:
        return redirect(url_for('admin_login'))
    
    if request.method == 'POST':
        yt_embed_link = request.form['yt_embed_link']

    try:
        new_video_link = ServiceVideo(description_id=description_id, yt_embed_link=yt_embed_link)
        db.session.add(new_video_link)
        db.session.commit()
        flash("Video link upload successfully.", "success")

    except Exception as e:
        db.session.rollback()
        flash(f"Failed to save Video link: {str(e)}", "danger")

    return redirect(request.referrer or url_for('admin_dashboard'))

# Deleting Service Video 
@app.route('/admin/delete_video_service/<id>', methods=['POST'])
def delete_video_service(id):
    if 'admin_id' not in session:
        return redirect(url_for('admin_login'))

    try:
        video_service_data = ServiceVideo.query.filter_by(id=id).first()
        video_filename = video_service_data.yt_embed_link
        delete_path = os.path.join(app.config['UPLOAD_FOLDER'], video_filename)

        db.session.delete(video_service_data)
        db.session.commit()

        if delete_path and os.path.exists(delete_path):
            try:
                os.remove(delete_path)
            except Exception as file_error:
                flash(f"Video path deleted, but Video file couldn't be removed: {file_error}", "warning")

        flash("Video deleted successfully.", "success")

    except Exception as e:
        db.session.rollback()
        flash(f"Error deleting service: {str(e)}", "danger")

    return redirect(request.referrer or url_for('admin_dashboard'))

# Delete contact us message
@app.route('/admin/delete_contact/<id>', methods=['POST'])
def delete_contact(id):
    if 'admin_id' not in session:
        return redirect(url_for('admin_login'))
    contact = Contact.query.filter_by(id=id).first()
    db.session.delete(contact)
    db.session.commit()
    flash('Contact us message deleted successfully', "success")

    return redirect(url_for('admin_dashboard'))


if __name__ == '__main__':
    app.run()