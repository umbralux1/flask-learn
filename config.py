class Configuaration:
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:1@localhost/test1'
    SECRET_KEY = 'something very secret'
