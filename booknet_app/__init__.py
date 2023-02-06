import os 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
db_user = os.environ.get('DB_USER')
db_pw = os.environ.get('DB_PW')

db_url = f"postgresql+psycopg2://{db_user}:{db_pw}@localhost:5432/booknet_db"

app.config['SQLALCHEMY_DATABASE_URI'] = db_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app,db)

login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "users.user_login"

#### Import all Blueprints ####
from booknet_app.core.routes import core
from booknet_app.users.routes import users
from booknet_app.books.routes import books
from booknet_app.stores.routes import stores
from booknet_app.bookshelves.routes import bookshelves
from booknet_app.error_pages.handlers import error_pages
from booknet_app.api.store_api import store_api

##### Register all blueprints #####
app.register_blueprint(core)
app.register_blueprint(users)
app.register_blueprint(books)
app.register_blueprint(stores)
app.register_blueprint(bookshelves)
app.register_blueprint(error_pages)
app.register_blueprint(store_api)
