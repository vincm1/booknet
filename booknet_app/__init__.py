import os 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

db_user_env = os.environ.get('DB_USER')
db_pw_env = os.environ.get('DB_PW')

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql+psycopg2://{db_user_env}:{db_pw_env}@localhost/booknet_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app,db)

### Twitter OAuth ###


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

##### Register all blueprints #####
app.register_blueprint(core)
app.register_blueprint(users)
app.register_blueprint(books)
app.register_blueprint(stores)
app.register_blueprint(bookshelves)
app.register_blueprint(error_pages)