from crypt import methods
from dataclasses import replace
from turtle import home
from webbrowser import get
from flask import Flask, render_template,url_for, request
import pickle
import numpy as np
from flask import Flask, render_template
from pip import main


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

@app.route('/')
@app.route('/home')
def index():
   return render_template('index.html')

@app.route('/form')
def form():
    return render_template('form.html')


@app.route('/', methods=['GET'])
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

