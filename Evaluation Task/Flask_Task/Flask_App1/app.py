from flask import Flask, render_template, request
import traceback
import sys

try:
    app = Flask(__name__)
    app.debug = True  # Enable debug mode

    @app.route("/")
    def home():
        return render_template('index.html')

    @app.route("/square", methods=['GET', 'POST'])
    def square():
        if request.method == 'POST':
            # Access the data from the form
            num = int(request.form["num"])
            output = num * num

            return render_template("index.html",input_number= num, square_number='Square is {}'.format(output))

    if __name__ == "__main__":
        app.run()

except Exception as e:
    traceback.print_exc()
    sys.exit(1)