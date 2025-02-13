import pytest
import json
from flask import app
from models import db, Book

@pytest.fixture
def client():
    """ Configura una aplicación de prueba en Flask """
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        with app.app_context():
            db.drop_all()

def test_get_books(client):
    """ Prueba obtener la lista de libros (debe ser vacía al inicio) """
    response = client.get("/books")
    assert response.status_code == 200
    assert response.get_json() == []

def test_add_book(client):
    """ Prueba agregar un libro nuevo """
    new_book = {
        "id": "1234abcd5678efgh",
        "title": "The Flask Journey",
        "author": "John Doe",
        "read_flag": False
    }
    response = client.post("/add/book", data=json.dumps(new_book), content_type="application/json")
    assert response.status_code == 201
    assert response.get_json()["title"] == "The Flask Journey"

def test_get_book_by_id(client):
    """ Prueba obtener un libro por ID """
    test_book = Book(id="test123", title="Test Book", author="Jane Doe", read_flag=True)
    with app.app_context():
        db.session.add(test_book)
        db.session.commit()

    response = client.get("/book/test123")
    assert response.status_code == 200
    assert response.get_json()["title"] == "Test Book"

def test_update_book(client):
    """ Prueba actualizar un libro existente """
    test_book = Book(id="update123", title="Old Title", author="Jane Doe", read_flag=False)
    with app.app_context():
        db.session.add(test_book)
        db.session.commit()

    update_data = {"title": "Updated Title", "author": "Jane Doe", "read_flag": True}
    response = client.put("/edit/book/update123", data=json.dumps(update_data), content_type="application/json")

    assert response.status_code == 200
    assert response.get_json()["title"] == "Updated Title"

def test_delete_book(client):
    """ Prueba eliminar un libro """
    test_book = Book(id="delete123", title="To Delete", author="Author", read_flag=False)
    with app.app_context():
        db.session.add(test_book)
        db.session.commit()

    response = client.delete("/delete/book/delete123")
    assert response.status_code == 200
    assert response.get_json() == {"message": "Book deleted"}

    response = client.get("/book/delete123")
    assert response.status_code == 404
