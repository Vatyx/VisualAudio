import os
from flask import Flask

app = Flask(__name__)
from app import main

app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)))