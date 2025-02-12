from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint
from config import Config
from models import db
from schemas import ma
from routes import book_bp

app = Flask(__name__, static_folder='static')
app.config.from_object(Config)

# Inicializar base de datos y Marshmallow
db.init_app(app)
ma.init_app(app)

# Registrar Blueprint de rutas
app.register_blueprint(book_bp)

# Configurar Swagger
SWAGGER_URL = "/swagger"
API_URL = "static/swagger.json"
swagger_ui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL)
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Crear la base de datos si no existe
    app.run(debug=True)
