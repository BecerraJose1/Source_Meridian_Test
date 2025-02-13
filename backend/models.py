from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Book(db.Model):
    __tablename__ = "book"  

    id = db.Column(db.String(32), primary_key=True, nullable=False)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    read_flag = db.Column(db.Boolean, default=False)

    def __init__(self, id, title, author, read_flag=False):
        self.id = id
        self.title = title
        self.author = author
        self.read_flag = read_flag
