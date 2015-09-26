from flask import render_template
from app import app
import myrdio

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}  # fake user
    myrdio.testFunction()
    return render_template('index.html')