#from flask import Flask, st, jsonify
import numpy as np
import pickle
import streamlit as st

model = pickle.load(open('./model1.pkl', 'rb'))

#app = Flask(__name__)

# @app.route('/')


def index():
    return "Hello world"


# @app.route('/predict', methods=['POST'])
def predict():

    st.title("Bank Authenticator")
    html_temp = """
        <div style="background-color:tomato;padding:10px">
        <h2 style="color:white;text-align:center;">Streamlit Bank Authenticator ML App </h2>
        </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    nitrogen = st.text_input('nitrogen', "")
    phosphorous = st.text_input('phosphorous', "")
    potassium = st.text_input('potassium', "")
    temp = st.text_input('temperature', "")
    humidity = st.text_input('humidity', "")
    ph = st.text_input('ph', "")
    rainfall = st.text_input('rainfall', "")
    result = ""
    ans = ""
    if st.button("Predict"):
        input_query = np.array(
            [[nitrogen, phosphorous, potassium, temp, humidity, ph, rainfall]])
        result = model.predict(input_query)
        ans = result[0]

    st.success('The output is {}'.format(ans))


if __name__ == '__main__':
    predict()
