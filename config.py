import os

DEBUT = True
PROJECT_DIR = os.path.dirname(os.path.abspath(__name__))
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = 'mysql://ganteng:achmadgozali@localhost/crud'