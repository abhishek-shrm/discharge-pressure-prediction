from flask import Flask,request,render_template
import pandas as pd
import numpy as np
from sklearn.externals import joblib

app=Flask(__name__)

model=joblib.load(open('../model.pkl','rb'))

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
  '''
    For rendering prediction result on index.html
  '''
  try:
    suction_temperature=float(request.form['suction_temperature'])
    total_flow=float(request.form['total_flow'])
    speed=float(request.form['speed'])
    valve_position=float(request.form['valve_position'])
    discharge_temp=float(request.form['discharge_temp'])
    suction_pressure=float(request.form['suction_pressure'])
    
    input_features=[suction_pressure,suction_temperature,total_flow,speed,valve_position,discharge_temp]
    final_features=np.array(input_features).reshape(1,-1)
    prediction=model.predict(final_features)
  
  except ValueError:
    return "Please check if the values are entered correctly"

  return render_template('index.html',prediction_text="Discharge Pressure (psig) = {}".format(prediction))

if __name__=="__main__":
  app.run(debug=True)