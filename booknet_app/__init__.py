import os 
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

db_user_env = os.environ.get('DB_USER')
db_pw_env = os.environ.get('DB_PW')

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql+psycopg2://{db_user_env}:{db_pw_env}@localhost/booknet_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app,db)

#### Import all Blueprints ####
from booknet_app.core.routes import core
from booknet_app.error_pages.handlers import error_pages


##### Register all blueprints #####
app.register_blueprint(core)
app.register_blueprint(error_pages)