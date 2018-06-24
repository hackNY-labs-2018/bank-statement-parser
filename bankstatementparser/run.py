import views
from werkzeug import import_string, cached_property
from flask import Flask
from views import app

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)
