from flask import Flask
from sqlmodel import create_engine
from .model import *
from dotenv import load_dotenv

import os

load_dotenv()

postgresql_url = f"postgresql://{os.environ.get('DB_USERNAME')}:{os.environ.get('DB_PASSWORD')}@" \
                 f"{os.environ.get('DB_HOST')}:{os.environ.get('DB_PORT')}/" \
                 f"{os.environ.get('DB_NAME')}"

engine = create_engine(postgresql_url, echo=True)


def create_app():
    app = Flask(__name__)

    from .route import product

    app.register_blueprint(product, url_prefix="/product")

    SQLModel.metadata.create_all(engine)
    return app
