'''
Run.py allows running the app directly from command line with 'python run.py'
'''

from app import app

if __name__ == '__main__':
    # make sure to set debug=False for production
    app.run()
