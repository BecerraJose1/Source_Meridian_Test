import os

class Config:
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:example@db:3306/books_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
