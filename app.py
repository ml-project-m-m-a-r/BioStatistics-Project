from dataclasses import replace
from turtle import home
from webbrowser import get
from flask import Flask, render_template,url_for, request
import pickle
import numpy as np
from flask import Flask, render_template
from pip import main

data=[]
y=None

def preProcess(x): 
    x["active"]=x["active"].replace("inactive", 0)
    x["active"]=x["active"].replace("active", 1) 
    # depends on data from Front
    return x


def load(x):
    model = pickle.load(open("trainedModel.sav",'rb')) 
    y=model.predict(np.array(x).reshape(1,-1))[0]
    return y

app= Flask(__name__)




@app.route('/form',  methods=['GET','POST'])
def form():
    print(request.form)

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
    
    if y:
        
    
    return render_template('form.html')
     

    # if request.form.get('age')!= None:
    #     data.clear()
    #     data.append(int(request.form.get('age')))
    #     data.append(int(request.form.get('height')))
    #     data.append(int(request.form.get('weight')))
    #     data.append(int(request.form.get('gender')))
    #     data.append(int(request.form.get('systolic')))
    #     data.append(int(request.form.get('diastolic')))
    #     data.append(int(request.form.get('cholesterol')))
    #     data.append(int(request.form.get('glucose')))
    #     data.append(int(request.form.get('smoking')))
    #     data.append(int(request.form.get('alcoholIntake')))
    #     data.append(int(request.form.get('physicalActivity')))
    #     y= load(data)
    #     print(y)
    # return render_template('form.html')
    
    
    
    

@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")

@app.route('/predict', methods=['GET','POST'])

def predict():
    if request=="POST":
        f= request.files("/file")
        x= preProcess(f)
        ####
        out =load(x)
        return out
    return None


if __name__ == "__main__":
    app.run(debug=True)

