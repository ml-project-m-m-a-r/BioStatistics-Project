from dataclasses import replace
from turtle import home
from webbrowser import get
from flask import Flask, render_template,url_for, request
import pickle
import numpy as np
from flask import Flask, render_template
from pip import main

data=[]
def load(x):
    model = pickle.load(open("trainedModel.sav",'rb')) 
    y=model.predict(np.array(x).reshape(1,-1))[0]
    return y

app= Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")


@app.route('/form',  methods=['GET','POST'])
def form():
    print(request.form)
    y=None
    if request.form.get('age')!= None:
        data.clear()
        data.append(int(float(request.form.get('age'))*12*30))
        data.append(int(request.form.get('gender')))
        data.append(int(request.form.get('height')))
        data.append(float(request.form.get('weight')))
        data.append(int(request.form.get('systolic')))
        data.append(int(request.form.get('diastolic')))
        data.append(int(request.form.get('cholesterol')))
        data.append(int(request.form.get('glucose')))
        data.append(int(request.form.get('smoking')))
        data.append(int(request.form.get('alcohol')))
        data.append(int(request.form.get('physicalActivity')))
        y= load(data)
        print(data)
        print(y)
    
    if y == 0:
        z="You don't have a cardiovascular disease!"
        l="Note: this statistics are not fully accurate, Please visit a doctor if something is wrong."
        return render_template('form.html',res=z, note=l)
    elif y==1:
        z="It appears that you might have a cardiovascular disease"
        l="Note: this statistics are not fully accurate, Please visit a doctor to check."
        return render_template('form.html',res=z,note=l)
    else:
        z="The Result Will Appear Here.."
        return render_template('form.html',res=z)
     

if __name__ == "__main__":
    app.run(debug=True)

