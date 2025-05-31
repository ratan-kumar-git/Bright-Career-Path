from flask import Flask, render_template


app = Flask(__name__)

# Home Page
@app.route('/')
def index():
    services = [
        {'url':'lms_solution', 'title': 'LMS Solutions', 'description': 'Streamline student management and learning with our smart, cloud-based Learning Management System tailored for schools and colleges.', 'image': 'images/lms.jpg'},
        {'url':'creative-extracurricular', 'title': 'Creative & Extracurricular', 'description': 'Unleash talent beyond academics with programs in art, craft, dance, drama, music, and sports designed to nurture holistic development.', 'image': 'images/creative-extracurricular1.jpg'},
        {'url':'digital_marketing', 'title': 'Digital Marketing', 'description': 'Grow your institution’s online presence with our tailored digital marketing services, including SEO, social media, and content campaigns.', 'image': 'images/digital-marketing.jpg'},
        {'url':'photography-videography', 'title': 'Photography & Videography', 'description': 'Capture moments that matter through professional photography, group photoshoots, and high-quality videography for your institution.', 'image': 'images/photo-video-graphy.jpg'},
        {'url':'career_counseling', 'title': 'Career Counseling', 'description': 'Guide students towards the right path with expert counseling for Classes 10, 12, undergraduate, postgraduate, diploma, and professional courses.', 'image': 'images/career-counseling.jpg'},
        {'url':'placement_support', 'title': 'Placement Support', 'description': 'Empower careers with real opportunities through our extensive private job network and dedicated placement advisory services.', 'image': 'images/placement-support.jpg'},
        {'url':'smart_class_infrastructure', 'title': 'Smart Class Infrastructure', 'description': 'Upgrade your classrooms with our tech-enabled smart class solutions—featuring interactive boards, digital content, projectors, and LMS integration to make learning more engaging and effective.', 'image': 'images/smart-class-infrastructure.jpg'},
        {'url':'animation', 'title': 'Animation', 'description': 'Ignite creativity with our animation training programs that teach students the fundamentals of 2D and 3D animation, visual storytelling, and digital design using industry-standard tools.', 'image': 'images/animation.jpg'},
        {'url':'summer-winter_camps', 'title': 'Summer & Winter Camps', 'description': 'Our seasonal camps offer a perfect mix of learning and fun through hands-on workshops, creative activities, sports, and life skills training—helping students explore new interests and grow holistically.', 'image': 'images/summer-winter-camps.jpg'},
        
    ]   
    contacts = [
        {'head_office_address': 'Mohaddiganj, Sasaram, Rohtas, Bihar', 'branch_office_address': 'Vijay Nagar, Indore, Madhya Pradesh', 'mob_no': '+91 7870767779', 'email': 'omtusharsingh78@gmail.com'}
    ]
    social_links = [
        {'insta': '#', 'fb': '#', 'yt': '#'}
    ]
    return render_template('home.html', title='Home | Bright Career Path', services=services, contacts=contacts, social_links=social_links, len=len)

# Services Page
@app.route('/services')
def services():
    services = [
        {'url':'lms_solution', 'title': 'LMS Solutions', 'description': 'Streamline student management and learning with our smart, cloud-based Learning Management System tailored for schools and colleges.', 'image': 'images/lms.jpg'},
        {'url':'creative-extracurricular', 'title': 'Creative & Extracurricular', 'description': 'Unleash talent beyond academics with programs in art, craft, dance, drama, music, and sports designed to nurture holistic development.', 'image': 'images/creative-extracurricular1.jpg'},
        {'url':'digital_marketing', 'title': 'Digital Marketing', 'description': 'Grow your institution’s online presence with our tailored digital marketing services, including SEO, social media, and content campaigns.', 'image': 'images/digital-marketing.jpg'},
        {'url':'photography-videography', 'title': 'Photography & Videography', 'description': 'Capture moments that matter through professional photography, group photoshoots, and high-quality videography for your institution.', 'image': 'images/photo-video-graphy.jpg'},
        {'url':'career_counseling', 'title': 'Career Counseling', 'description': 'Guide students towards the right path with expert counseling for Classes 10, 12, undergraduate, postgraduate, diploma, and professional courses.', 'image': 'images/career-counseling.jpg'},
        {'url':'placement_support', 'title': 'Placement Support', 'description': 'Empower careers with real opportunities through our extensive private job network and dedicated placement advisory services.', 'image': 'images/placement-support.jpg'},
        {'url':'smart_class_infrastructure', 'title': 'Smart Class Infrastructure', 'description': 'Upgrade your classrooms with our tech-enabled smart class solutions—featuring interactive boards, digital content, projectors, and LMS integration to make learning more engaging and effective.', 'image': 'images/smart-class-infrastructure.jpg'},
        {'url':'animation', 'title': 'Animation', 'description': 'Ignite creativity with our animation training programs that teach students the fundamentals of 2D and 3D animation, visual storytelling, and digital design using industry-standard tools.', 'image': 'images/animation.jpg'},
        {'url':'summer-winter_camps', 'title': 'Summer & Winter Camps', 'description': 'Our seasonal camps offer a perfect mix of learning and fun through hands-on workshops, creative activities, sports, and life skills training—helping students explore new interests and grow holistically.', 'image': 'images/summer-winter-camps.jpg'},
        
    ]
    return render_template('services.html', title='Our Services', services=services, len=len)

def find_service(name) :
    services = [
        {'url':'lms_solution', 'title': 'LMS Solutions', 'description': 'Streamline student management and learning with our smart, cloud-based Learning Management System tailored for schools and colleges.', 'image': 'images/lms.jpg'},
        {'url':'creative-extracurricular', 'title': 'Creative & Extracurricular', 'description': 'Unleash talent beyond academics with programs in art, craft, dance, drama, music, and sports designed to nurture holistic development.', 'image': 'images/creative-extracurricular1.jpg'},
        {'url':'digital_marketing', 'title': 'Digital Marketing', 'description': 'Grow your institution’s online presence with our tailored digital marketing services, including SEO, social media, and content campaigns.', 'image': 'images/digital-marketing.jpg'},
        {'url':'photography-videography', 'title': 'Photography & Videography', 'description': 'Capture moments that matter through professional photography, group photoshoots, and high-quality videography for your institution.', 'image': 'images/photo-video-graphy.jpg'},
        {'url':'career_counseling', 'title': 'Career Counseling', 'description': 'Guide students towards the right path with expert counseling for Classes 10, 12, undergraduate, postgraduate, diploma, and professional courses.', 'image': 'images/career-counseling.jpg'},
        {'url':'placement_support', 'title': 'Placement Support', 'description': 'Empower careers with real opportunities through our extensive private job network and dedicated placement advisory services.', 'image': 'images/placement-support.jpg'},
        {'url':'smart_class_infrastructure', 'title': 'Smart Class Infrastructure', 'description': 'Upgrade your classrooms with our tech-enabled smart class solutions—featuring interactive boards, digital content, projectors, and LMS integration to make learning more engaging and effective.', 'image': 'images/smart-class-infrastructure.jpg'},
        {'url':'animation', 'title': 'Animation', 'description': 'Ignite creativity with our animation training programs that teach students the fundamentals of 2D and 3D animation, visual storytelling, and digital design using industry-standard tools.', 'image': 'images/animation.jpg'},
        {'url':'summer-winter_camps', 'title': 'Summer & Winter Camps', 'description': 'Our seasonal camps offer a perfect mix of learning and fun through hands-on workshops, creative activities, sports, and life skills training—helping students explore new interests and grow holistically.', 'image': 'images/summer-winter-camps.jpg'},
        
    ]
    length_services = len(services)
    for i in range(length_services):
        if services[i]['url'] == name:
            service = services[i]
            return service


# Services_page Page
@app.route('/services/<name>')
def services_page(name):
    services = find_service(name)
    videos = [
        {'yt_video': '''<iframe class="rounded-lg w-full h-full" src="https://www.youtube.com/embed/OtJV9SCyfuE?si=D-uqTbR2sJage3XV"
                    title="YouTube video player" frameborder="0"
                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
                    referrerpolicy="strict-origin-when-cross-origin" allowfullscreen>
                </iframe>'''},
        {'yt_video': '''<iframe class="rounded-lg w-full h-full" src="https://www.youtube.com/embed/OtJV9SCyfuE?si=D-uqTbR2sJage3XV"
                    title="YouTube video player" frameborder="0"
                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
                    referrerpolicy="strict-origin-when-cross-origin" allowfullscreen>
                </iframe>'''},
        {'yt_video': '''<iframe class="rounded-lg w-full h-full" src="https://www.youtube.com/embed/OtJV9SCyfuE?si=D-uqTbR2sJage3XV"
                    title="YouTube video player" frameborder="0"
                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
                    referrerpolicy="strict-origin-when-cross-origin" allowfullscreen>
                </iframe>'''},
        {'yt_video': '''<iframe class="rounded-lg w-full h-full" src="https://www.youtube.com/embed/OtJV9SCyfuE?si=D-uqTbR2sJage3XV"
                    title="YouTube video player" frameborder="0"
                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
                    referrerpolicy="strict-origin-when-cross-origin" allowfullscreen>
                </iframe>'''},
        {'yt_video': '''<iframe class="rounded-lg w-full h-full" src="https://www.youtube.com/embed/OtJV9SCyfuE?si=D-uqTbR2sJage3XV"
                    title="YouTube video player" frameborder="0"
                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
                    referrerpolicy="strict-origin-when-cross-origin" allowfullscreen>
                </iframe>'''},
        {'yt_video': '''<iframe class="rounded-lg w-full h-full" src="https://www.youtube.com/embed/OtJV9SCyfuE?si=D-uqTbR2sJage3XV"
                    title="YouTube video player" frameborder="0"
                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
                    referrerpolicy="strict-origin-when-cross-origin" allowfullscreen>
                </iframe>'''}
    ]
    return render_template('services_page.html', title=f'{name} | Service', services=services, name=name, len= len, videos=videos)

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