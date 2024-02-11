import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://kib:Kibiego22@localhost/market'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = os.urandom(24) 