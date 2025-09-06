from flask import Flask

def create_app():
    app = Flask(__name__)

    # register blueprints
    from .routes import bp as main_bp
    app.register_blueprint(main_bp)

    return app
