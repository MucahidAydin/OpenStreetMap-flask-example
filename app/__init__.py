from flask import Flask, redirect, url_for
from config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    from app.main import bp as main_bp

    app.register_blueprint(main_bp, url_prefix="/geo")

    @app.route("/")
    def index():
        data = {
            "center_x": 41.0082,
            "center_y": 28.9784,
            "zoom": 5,
        }
        return redirect(url_for("main.geo_loc", **data))

    return app
