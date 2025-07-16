import os

class Config:
    """
    Configuration class for the application.
    """
    SECRET_KEY = 'e9a3c75a6cf3e587b7648f9440749256'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')