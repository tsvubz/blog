from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from app.config import Config


db = SQLAlchemy() #Initialize the database, instance of SQLAlchemy
bcrypt = Bcrypt() #Initialize the bcrypt instance for password hashing
login_manager = LoginManager() #Initialize the login manager for user sessions
login_manager.login_view = 'users.login' #Set the login view for the login manager
login_manager.login_message_category = 'info'

mail = Mail() #Initialize the mail instance for sending emails



def create_app(config_class=Config):
    """
    Factory function to create and configure the Flask application.
    """
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from app.users.routes import users
    from app.posts.routes import posts
    from app.main.routes import main
    from app.errors.handlers import errors

    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app