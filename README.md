# bank-statement-parser

Dev
---

Setup:

    virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt
    python generate_secret.py  # save the output generated here for the next step

Create a new directory `instance` and then create a new file `instance/config.py` with the following contents:

    SECRET = b'xxx'
    DEBUG = True

replacing `b'xxx'` with the secret key you generated above.

Running:

    python run.py   # flask automatically reloads on changes

Go to  `localhost:5000`

Wiki
---
Built with [Flask](http://flask.pocoo.org/) and [pdf.js](https://github.com/mozilla/pdf.js)

Directory structure:
- `\instance` stores all data(eg. config, uploaded files) about current running server
- `app\templates` has all html
- `app\static` has all js/css/static files
