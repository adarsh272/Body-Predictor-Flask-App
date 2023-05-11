def predict_body_type():
    age = float(request.form['age'])
    gender = float(request.form['gender'])
    height = float(request.form['height'])
    weight = float(request.form['weight'])
    body_fat = float(request.form['body-fat'])
    diastolic = float(request.form['diastolic-bp'])
    systolic = float(request.form['systolic-bp'])
    situps = float(request.form['sit-ups'])
    jump = float(request.form['jump-distance'])

    result = model.predict(np.array([age, gender, height, weight, body_fat, diastolic, systolic, situps, jump]).reshape(1,3))

    return str(result)