import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'postgresql://root:root@172.17.0.1/my_database'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

