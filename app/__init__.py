from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = 'e9a3c75a6cf3e587b7648f9440749256'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app) #Initialize the database, instance of SQLAlchemy
bcrypt = Bcrypt(app) #Initialize the bcrypt instance for password hashing
login_manager = LoginManager(app) #Initialize the login manager for user sessions
login_manager.login_view = 'login' #Set the login view for the login manager
login_manager.login_message_category = 'info'

from app import routes