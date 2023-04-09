from flask import Flask, request, jsonify
import numpy as np
import pickle

model = pickle.load(open('./model1.pkl', 'rb'))

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello world"


@app.route('/predict', methods=['POST'])
def predict():

    nitrogen = request.form.get('nitrogen')
    phosphorous = request.form.get('phosphorous')
    potassium = request.form.get('potassium')
    temp = request.form.get('temperature')
    humidity = request.form.get('humidity')
    ph = request.form.get('ph')
    rainfall = request.form.get('rainfall')

    input_query = np.array(
        [[nitrogen, phosphorous, potassium, temp, humidity, ph, rainfall]])

    result = model.predict(input_query)

    return jsonify({'Result': str(result)})


if __name__ == '__main__':
    app.run(debug=True)
