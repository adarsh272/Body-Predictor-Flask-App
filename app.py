from flask import Flask, render_template, request
import pickle
import numpy as np
import gdown

url = 'https://drive.google.com/uc?id=13Ssu06MYb8Ek1_bTZPNwZTP6tL7wv-UV'
output = 'model.pkl'
gdown.download(url, output, quiet=False)
model = pickle.load(open('model.pkl', 'rb'))


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])

def predict_body_type():
    age = float(request.form['age'])
    gender = int(request.form['gender'])
    height = float(request.form['height'])
    weight = float(request.form['weight'])
    body_fat = float(request.form['body-fat'])
    diastolic = float(request.form['diastolic-bp'])
    systolic = float(request.form['systolic-bp'])
    situps = float(request.form['sit-ups'])
    jump = float(request.form['jump-distance'])
    grip_force = float(request.form['grip-strength'])
    sit_bend = float(request.form['sit-bend-distance'])
    bmi = weight / ((height/100) ** 2)
    health_status = ''

    if bmi < 18.5:
        health_status = "Underweight";
    elif bmi < 25:
        health_status = "Healthy";
    elif bmi < 30:
        health_status = "Overweight";
    else :
     health_status = "Obese";
  

    result = model.predict(np.array([age, height, weight, body_fat, diastolic, systolic, grip_force, sit_bend, situps, jump, gender]).reshape(1,11))

    return render_template('result.html', bmi=bmi, weight=weight, height=height, health_status=health_status, diastolic=diastolic, systolic=systolic, situps=situps, body_fat=body_fat,sit_bend=sit_bend, result=result[0])

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)