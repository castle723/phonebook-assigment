import os
from dotenv import load_dotenv
basedir = os.path.abspath(os.path.dirname(__file__))
load_doenv(os.path.join(basedir, '.env'))

class Config():
    '''
        set config variables for the flask app
        using environment variable where available.
        Otherwise, create the config variable if not done already.
    '''

    FLASK_APP = os.getenv('FLASK_APP')
    FLASK_ENV = os.getenv('FLASK_ENV')
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'ryan will never get access to my CSS'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqllite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_NOTIFICATIONS = False                      