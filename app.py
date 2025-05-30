from flask import Flask, render_template


app = Flask(__name__)

# Home Page
@app.route('/')
def index():
    services = [
        {'title': 'Digital Marketing', 'description': 'Odio excepturi sequi at ullam fugiat iusto nemo debitis nostrum eveniet soluta beatae, perferendis doloremque sapiente molestiae iure eum incidunt? Minus, nobis.', 'image': 'images/image-1.jpg'},
        {'title': 'Digital Marketing', 'description': 'Odio excepturi sequi at ullam fugiat iusto nemo debitis nostrum eveniet soluta beatae, perferendis doloremque sapiente molestiae iure eum incidunt? Minus, nobis.', 'image': 'images/image-1.jpg'},
        {'title': 'Digital Marketing', 'description': 'Odio excepturi sequi at ullam fugiat iusto nemo debitis nostrum eveniet soluta beatae, perferendis doloremque sapiente molestiae iure eum incidunt? Minus, nobis.', 'image': 'images/image-1.jpg'},
        {'title': 'Digital Marketing', 'description': 'Odio excepturi sequi at ullam fugiat iusto nemo debitis nostrum eveniet soluta beatae, perferendis doloremque sapiente molestiae iure eum incidunt? Minus, nobis.', 'image': 'images/image-1.jpg'},
        {'title': 'Digital Marketing', 'description': 'Odio excepturi sequi at ullam fugiat iusto nemo debitis nostrum eveniet soluta beatae, perferendis doloremque sapiente molestiae iure eum incidunt? Minus, nobis.', 'image': 'images/image-1.jpg'},
        {'title': 'Digital Marketing', 'description': 'Odio excepturi sequi at ullam fugiat iusto nemo debitis nostrum eveniet soluta beatae, perferendis doloremque sapiente molestiae iure eum incidunt? Minus, nobis.', 'image': 'images/image-1.jpg'},
        
    ]
    return render_template('home.html', title='Home | Bright Career Path', services=services)
    
if __name__ == '__main__':
    app.run(debug=True)