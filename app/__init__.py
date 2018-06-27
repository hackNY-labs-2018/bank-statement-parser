'''
This file initiates the flask app
'''

from flask import Flask

# Initialize the app
app = Flask(__name__, instance_relative_config=True)

# Load the views
from app import views

# Load the config file from config.py
app.config.from_object('config')