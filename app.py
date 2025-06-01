from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import bcrypt


app = Flask(__name__)

# DB Connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///services.db'
db = SQLAlchemy(app)

app.secret_key = 'Bablu@12345'

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
    for img in services_page_img:
        print("Image:", img.img_filename)

    for vid in services_page_video:
        print("Video:", vid.yt_embed_link)

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
@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact')

   
if __name__ == '__main__':
    app.run(debug=True)