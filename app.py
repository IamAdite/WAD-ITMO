from flask import Flask
from flask import render_template, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return redirect("/profile")

@app.errorhandler(404)
def page_not_found(e):
    return redirect('/profile')

@app.route('/profile')
def hello_world():
    return render_template('index.html')
