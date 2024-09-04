# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate

from app import config
Config = config.Config
app = Flask(__name__)
app.config['SECRET_KEY']  = '95371e2f-a487-4e22-a9e2-8b6356b85454'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # Example: Change as per your DB configuration
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

login_manager = LoginManager(app)
login_manager.login_view = "users.login"
bcrypt = Bcrypt(app)



login_manager.login_view = 'login'

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

from app import routes, models
# from app.models import User