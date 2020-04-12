from flask import Flask

from config import Configuaration

app = Flask(__name__)
app.config.from_object(Configuaration)
