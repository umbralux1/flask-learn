from flask import Flask

from config import Configuaration
from posts.blueprint import posts

app = Flask(__name__)
app.config.from_object(Configuaration)
app.register_blueprint(posts, url_prefix='/blog')
