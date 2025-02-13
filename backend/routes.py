import uuid
from flask import Blueprint, request, jsonify
from models import db, Book
from schemas import BookSchema

book_bp = Blueprint('books', __name__)
book_schema = BookSchema()
books_schema = BookSchema(many=True)

# Obtener todos los libros
@book_bp.route('/books', methods=['GET'])
def get_books():
    books = Book.query.all()
    return books_schema.dump(books)

# Obtener un libro por ID
@book_bp.route('/book/<string:book_id>', methods=['GET'])
def get_book(book_id):
    book = Book.query.get(book_id)
    if not book:
        return jsonify({'message': 'Book not found'}), 404
    return book_schema.jsonify(book)

# Agregar un nuevo libro
@book_bp.route('/add/book', methods=['POST'])
def add_book():
    data = request.json
    new_book = Book(
        id=str(uuid.uuid4().hex),
        title=data['title'],
        author=data['author'],
        read_flag=data.get('read_flag', False)
    )
    db.session.add(new_book)
    db.session.commit()
    return book_schema.dump(new_book), 201

# Editar un libro
@book_bp.route('/edit/book/<string:book_id>', methods=['PUT'])
def update_book(book_id):
    book = Book.query.get(book_id)
    if not book:
        return jsonify({'message': 'Book not found'}), 404
    
    data = request.json
    book.title = data.get('title', book.title)
    book.author = data.get('author', book.author)
    book.read_flag = data.get('read_flag', book.read_flag)

    db.session.commit()
    return book_schema.dump(book)

# Eliminar un libro
@book_bp.route('/delete/book/<string:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = Book.query.get(book_id)
    if not book:
        return jsonify({'message': 'Book not found'}), 404

    db.session.delete(book)
    db.session.commit()
    return jsonify({'message': 'Book deleted'})
