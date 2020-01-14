from .config import Config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
#from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
app.debug = True


db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

#migrate = Migrate(app, db)


from . import views
