import os

from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY", "secret_key_123")

from exam_estimate import controllers
from exam_estimate import jinja_filters
