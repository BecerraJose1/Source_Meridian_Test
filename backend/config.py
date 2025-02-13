import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "mysql+pymysql://root:example123@db:3506/db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
