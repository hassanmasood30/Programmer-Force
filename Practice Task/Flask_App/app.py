from flask import Flask, render_template, request
import pickle
import traceback
import sys

try:
    app = Flask(__name__)
    app.debug = True  # Enable debug mode

    model = pickle.load(open('expense_model.pkl', 'rb'))  # read mode

    @app.route("/")
    def home():
        return render_template('index.html')

    @app.route("/predict", methods=['GET', 'POST'])
    def predict():
        if request.method == 'POST':
            # Access the data from the form
            age = int(request.form["age"])
            bmi = int(request.form["bmi"])
            children = int(request.form["children"])
            Sex = int(request.form["Sex"])
            Smoker = int(request.form["Smoker"])
            Region = int(request.form["Region"])

            # Get prediction
            input_cols = [[age, bmi, children, Sex, Smoker, Region]]
            prediction = model.predict(input_cols)
            output = round(prediction[0], 2)
            return render_template("index.html", prediction_text='Your predicted annual Healthcare Expense is $ {}'.format(output))

    if __name__ == "__main__":
        app.run()

except Exception as e:
    traceback.print_exc()
    sys.exit(1)