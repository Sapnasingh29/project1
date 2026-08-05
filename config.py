import os

class Config:
    SECRET_KEY = "your-secret-key"

    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, "instance", "employee.db")

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    