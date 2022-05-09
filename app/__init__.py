from flask import Flask
from config import DevelopmentConfig
    
def create_app(config = DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config)

    # register apps
    from app.importation import importation_bp
    
    app.register_blueprint(importation_bp)
    return app