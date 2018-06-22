from flask import Flask, request, render_template, redirect, url_for, flash
from werkzeug import import_string, cached_property

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        print ('hello')
        return 'henlo worl'
