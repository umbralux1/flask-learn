from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import Configuaration

app = Flask(__name__)
app.config.from_object(Configuaration)

db = SQLAlchemy(app)
