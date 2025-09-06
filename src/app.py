from flask import Flask
from dotenv import load_dotenv
import os

def create_app():
    load_dotenv()  # load .env into process env

    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev-secret")

    from .routes import bp as main_bp
    app.register_blueprint(main_bp)
    return app
