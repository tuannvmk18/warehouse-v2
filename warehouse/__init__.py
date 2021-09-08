from flask import Flask
from sqlmodel import create_engine
from .model import *
from dotenv import load_dotenv
from flask_marshmallow import Marshmallow
import os

load_dotenv()

postgresql_url = f"postgresql://{os.environ.get('DB_USERNAME')}:{os.environ.get('DB_PASSWORD')}@" \
                 f"{os.environ.get('DB_HOST')}:{os.environ.get('DB_PORT')}/" \
                 f"{os.environ.get('DB_NAME')}"

engine = create_engine(postgresql_url, echo=True)
ma = Marshmallow()


def create_app():
    app = Flask(__name__)
    ma.init_app(app)
    from .route import product, supplier, order

    app.register_blueprint(product, url_prefix="/product")
    app.register_blueprint(supplier, url_prefix="/supplier")
    app.register_blueprint(order, url_prefix="/order")

    SQLModel.metadata.create_all(engine)
    return app
