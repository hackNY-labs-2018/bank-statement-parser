'''
Views.py holds all views of the app
'''


from flask import request, render_template, redirect, url_for, flash, send_from_directory
from werkzeug.utils import secure_filename

from app import app
import os

# NOTE: Flask defaults to serving html out of /templates, statics (js/css) out of /static

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template("index.html")

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() == 'pdf'

'''
Serves csv file to front-end
'''
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.instance_path, filename)

@app.route('/upload', methods=['POST'])
def api():
    # check if the post request has the file part
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    # if user does not select file, browser also
    # submit an empty part without filename
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)

    if file and allowed_file(file.filename):
        print('File received from upload successfully.')
        # http://werkzeug.pocoo.org/docs/0.14/utils/#werkzeug.utils.secure_filename
        filename = secure_filename(file.filename)
        # os.path.join is os-independent
        # saves to /instance
        newfile = os.path.join(app.instance_path, filename)
        print(newfile)
        file.save(newfile)
        print('File saved successfully.')
        return redirect(url_for('uploaded_file', filename=filename))
