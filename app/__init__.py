from flask import Flask
from ..config import DevelopmentConfig

def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)

    from .main.routes import main
    app.register_blueprint(main)

    from .email_service.email import email
    app.register_blueprint(email)

    return app