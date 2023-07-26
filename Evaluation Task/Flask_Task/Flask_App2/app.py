from flask import Flask, render_template, request
import traceback
import sys
import hashlib

try:
    app = Flask(__name__)
    app.debug = True  # Enable debug mode

    @app.route("/")
    def home():
        return render_template('index.html')
    
    @app.route('/md5', methods=['POST'])
    def md5():
        if 'image' not in request.files:
            return render_template(({'error': 'No image provided'}, 400))
        
        image_file = request.files['image']
        im_bytes = image_file.read()
        im_hash = hashlib.md5(im_bytes).hexdigest()
        return render_template('index.html',image = ({'md5_hash is': im_hash}, 200))

    if __name__ == "__main__":
        app.run()

except Exception as e:
    traceback.print_exc()
    sys.exit(1)