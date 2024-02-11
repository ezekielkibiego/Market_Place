# app/__init__.py

from flask import Flask
from app.config import Config

app = Flask(__name__)
app.config.from_object(Config)

from app.models import db
db.init_app(app)

from flask_migrate import Migrate
migrate = Migrate(app, db)

from flask_restful import Api
api = Api(app)

from api import ProductListResource

# Add API resources
api.add_resource(ProductListResource, '/api/products')

app.secret_key = Config.SECRET_KEY

from app import routes

from app import models
