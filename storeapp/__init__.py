from flask import Flask


def create_app():
    app = Flask(__name__)

    from storeapp.routes import api_bp
    app.register_blueprint(api_bp, url_prefix='/api/v1')

    return app

app = create_app()