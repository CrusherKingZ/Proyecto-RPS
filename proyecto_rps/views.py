from proyecto_rps import app

from flask import render_template

@app.route('/')
def index():
    return "<h1>Ready to go</h1>"

@app.route('/home')
def home_page():
    return render_template("home.html")