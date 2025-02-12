import os

class Config:
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:example123@localhost:3306/db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
