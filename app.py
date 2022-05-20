from flask import Flask, render_template
from pip import main
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
   return render_template('index.html')

@app.route('/form')
def form():
    return render_template('form.html')

if __name__ == '__main__':
   app.run()