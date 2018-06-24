from flask import Flask, request, render_template, redirect, url_for, flash
from werkzeug import import_string, cached_property

app = Flask(__name__)
# Flask defaults to serving html out of /templates, statics (js/css) out of /static

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template("index.html")
