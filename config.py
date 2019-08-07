import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # MAIL_SERVER = os.environ.get('MAIL_SERVER')
    # MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    # MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    # MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    # MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    # MAIL_ADMIN = os.environ.get('MAIL_ADMIN')
    # ADMINS = [MAIL_ADMIN]
    MAIL_SERVER = "smtp.googlemail.com"
    MAIL_PORT = "587"
    MAIL_USE_TLS = "1"
    MAIL_USERNAME = "snailmaildaemon"
    MAIL_PASSWORD = "Shoreland#19#"
    MAIL_ADMIN = "snailmaildaemon@gmail.com"
    ADMINS = [MAIL_ADMIN]
    POSTS_PER_PAGE = 25
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')
