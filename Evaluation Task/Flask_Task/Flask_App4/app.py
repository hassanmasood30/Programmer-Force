import traceback
from flask import Flask, render_template
from flask import request

class ML:
    def __init__(self):
        self.available_models = {
            "face_detection": "/additional_drive/ML/face_detection",
            "car_detection": "/additional_drive/ML/car_detection",
            "shoe_detection": "/additional_drive/ML/shoe_detection",
            "cloth_detection": "/additional_drive/ML/cloth_detection",
            "signal_detection": "/additional_drive/ML/signal_detection",
            "water_level_detection": "/additional_drive/ML/water_level_detection",
            "missile_detection": "/additional_drive/ML/missile_detection"
        }

        self.loaded_models_limit = 2
        #self.loaded_models = {}
        self.loaded_models = {
            model: self.load_weights(model)
            for model in list(self.available_models)[:self.loaded_models_limit]
        }

    def load_weights(self, model):
        return self.available_models.get(model, None)

    def load_balancer(self, new_model):
        print(self.loaded_models)
        if len(self.loaded_models) >= self.loaded_models_limit:
            least_used_model = min(self.loaded_models, key=self.loaded_models.get)
            self.loaded_models.pop(least_used_model)
        self.loaded_models[new_model] = self.load_weights(new_model)

app = Flask(__name__)
ml = ML()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_loaded_models', methods=['GET', 'POST'])
def get_loaded_models():
    return ml.loaded_models

@app.route('/process_request', methods=['GET', 'POST'])
def process_request():
    try:
        model = request.form["model"]
        if model not in ml.loaded_models:
            ml.load_balancer(model)
        return "processed by " + ml.loaded_models[model]
    except:
        return str(traceback.format_exc())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
