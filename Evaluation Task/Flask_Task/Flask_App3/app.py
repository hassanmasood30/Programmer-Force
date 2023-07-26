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
    
    @app.route('/table', methods=['POST'])
    def table():
        if request.method == 'POST':
            # Access the data from the form
            num = int(request.form["num"])
            table = [num * i for i in range(1, 11)]
            return render_template("index.html", table='Table : {}'.format(table))

    if __name__ == "__main__":
        app.run()

except Exception as e:
    traceback.print_exc()
    sys.exit(1)