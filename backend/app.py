from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint
from flask_cors import CORS  
from config import Config
from models import db
from schemas import ma
from routes import book_bp

app = Flask(__name__, static_folder='static')
app.config.from_object(Config)

CORS(app, resources={r"/*": {"origins": "*"}})  

db.init_app(app)
ma.init_app(app)

app.register_blueprint(book_bp)

# Configurar Swagger #TODO
SWAGGER_URL = "/swagger"
API_URL = "static/swagger.json"
swagger_ui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL)
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  
    app.run(debug=True)
