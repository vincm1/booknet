import os 
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

#### Import all Blueprints ####
from booknet_app.core.routes import core
from booknet_app.error_pages.handlers import error_pages


##### Register all blueprints #####
app.register_blueprint(core)
app.register_blueprint(error_pages)