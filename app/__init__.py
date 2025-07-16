import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)

app.config['SECRET_KEY'] = 'e9a3c75a6cf3e587b7648f9440749256'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app) #Initialize the database, instance of SQLAlchemy
bcrypt = Bcrypt(app) #Initialize the bcrypt instance for password hashing
login_manager = LoginManager(app) #Initialize the login manager for user sessions
login_manager.login_view = 'login' #Set the login view for the login manager
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
mail = Mail(app) #Initialize the mail instance for sending emails

from app import routes