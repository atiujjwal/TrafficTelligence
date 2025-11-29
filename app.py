import numpy as np
import pickle
import joblib
import matplotlib
import matplotlib.pyplot as plt
import time
import pandas as pd
import os
from flask import Flask, request, jsonify, render_template, redirect, url_for


app = Flask(__name__)

# Construct the path to the model file relative to the app's location
model_path = os.path.join(os.path.dirname(__file__), 'model', 'model.pkl')
with open(model_path, "rb") as model_file:
    model = pickle.load(model_file)

# Construct the path to the scaler file relative to the app's location
scaler_path = os.path.join(os.path.dirname(__file__), 'model', 'scaler.pkl')
with open(scaler_path, "rb") as scale_file:
    scale = pickle.load(scale_file)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    #fetching the posted data using request
    input_feature = [float(x) for x in request.form.values()]
    print(input_feature)
    features_values = [np.array(input_feature)]
    names = ['holiday', 'temp', 'rain', 'snow', 'weather', 'Day', 'Month', 'Year', 'Hours', 'Minutes', 'Seconds']
    data = pd.DataFrame(features_values, columns=names)
    data = scale.transform(data)
    data = pd.DataFrame(data, columns=names)
    #getting the prediction 
    prediction = model.predict(data)
    print(prediction)
    text = "Estimated Traffic volume is: " + str(prediction[0])
    print(text)
    return render_template("indexh.html", prediction_text=text)



if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(port=port, debug=True, use_reloader=False)
