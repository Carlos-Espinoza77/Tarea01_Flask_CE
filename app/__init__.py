from flask import Flask
from app.config import Config
from app.database import Base, engine


def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(Config)

    with app.app_context():
        from app.database import models
        Base.metadata.create_all(bind=engine)

        from app.routes import main_bp
        app.register_blueprint(main_bp)
        return app
