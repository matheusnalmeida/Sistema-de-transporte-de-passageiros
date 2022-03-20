from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt()

from flask_login import LoginManager
login_manager = LoginManager()