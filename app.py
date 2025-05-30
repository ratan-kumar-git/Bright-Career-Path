from flask import Flask, render_template


app = Flask(__name__)

# Home Page
@app.route('/')
def index():
    services = [
        {'title': 'LMS Solutions', 'description': 'Streamline student management and learning with our smart, cloud-based Learning Management System tailored for schools and colleges.', 'image': 'images/lms.jpg'},
        {'title': 'Creative & Extracurricular', 'description': 'Unleash talent beyond academics with programs in art, craft, dance, drama, music, and sports designed to nurture holistic development.', 'image': 'images/creative-extracurricular1.jpg'},
        {'title': 'Digital Marketing', 'description': 'Grow your institution’s online presence with our tailored digital marketing services, including SEO, social media, and content campaigns.', 'image': 'images/digital-marketing.jpg'},
        {'title': 'Photography & Videography', 'description': 'Capture moments that matter through professional photography, group photoshoots, and high-quality videography for your institution.', 'image': 'images/photo-video-graphy.jpg'},
        {'title': 'Career Counseling', 'description': 'Guide students towards the right path with expert counseling for Classes 10, 12, undergraduate, postgraduate, diploma, and professional courses.', 'image': 'images/career-counseling.jpg'},
        {'title': 'Placement Support', 'description': 'Empower careers with real opportunities through our extensive private job network and dedicated placement advisory services.', 'image': 'images/placement-support.jpg'},
        {'title': 'Smart Class Infrastructure', 'description': 'Upgrade your classrooms with our tech-enabled smart class solutions—featuring interactive boards, digital content, projectors, and LMS integration to make learning more engaging and effective.', 'image': 'images/smart-class-infrastructure.jpg'},
        {'title': 'Animation', 'description': 'Ignite creativity with our animation training programs that teach students the fundamentals of 2D and 3D animation, visual storytelling, and digital design using industry-standard tools.', 'image': 'images/animation.jpg'},
        {'title': 'Summer & Winter Camps', 'description': 'Our seasonal camps offer a perfect mix of learning and fun through hands-on workshops, creative activities, sports, and life skills training—helping students explore new interests and grow holistically.', 'image': 'images/summer-winter-camps.jpg'},
        
    ]
    return render_template('home.html', title='Home | Bright Career Path', services=services)

# Services Page
@app.route('/services')
def services():
    services = [
        {'title': 'LMS Solutions', 'description': 'Streamline student management and learning with our smart, cloud-based Learning Management System tailored for schools and colleges.', 'image': 'images/lms.jpg'},
        {'title': 'Creative & Extracurricular', 'description': 'Unleash talent beyond academics with programs in art, craft, dance, drama, music, and sports designed to nurture holistic development.', 'image': 'images/creative-extracurricular1.jpg'},
        {'title': 'Digital Marketing', 'description': 'Grow your institution’s online presence with our tailored digital marketing services, including SEO, social media, and content campaigns.', 'image': 'images/digital-marketing.jpg'},
        {'title': 'Photography & Videography', 'description': 'Capture moments that matter through professional photography, group photoshoots, and high-quality videography for your institution.', 'image': 'images/photo-video-graphy.jpg'},
        {'title': 'Career Counseling', 'description': 'Guide students towards the right path with expert counseling for Classes 10, 12, undergraduate, postgraduate, diploma, and professional courses.', 'image': 'images/career-counseling.jpg'},
        {'title': 'Placement Support', 'description': 'Empower careers with real opportunities through our extensive private job network and dedicated placement advisory services.', 'image': 'images/placement-support.jpg'},
        {'title': 'Smart Class Infrastructure', 'description': 'Upgrade your classrooms with our tech-enabled smart class solutions—featuring interactive boards, digital content, projectors, and LMS integration to make learning more engaging and effective.', 'image': 'images/smart-class-infrastructure.jpg'},
        {'title': 'Animation', 'description': 'Ignite creativity with our animation training programs that teach students the fundamentals of 2D and 3D animation, visual storytelling, and digital design using industry-standard tools.', 'image': 'images/animation.jpg'},
        {'title': 'Summer & Winter Camps', 'description': 'Our seasonal camps offer a perfect mix of learning and fun through hands-on workshops, creative activities, sports, and life skills training—helping students explore new interests and grow holistically.', 'image': 'images/summer-winter-camps.jpg'},
        
    ]
    return render_template('services.html', title='Our Services', services=services)

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