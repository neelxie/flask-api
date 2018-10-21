from flask import Flask
#from config import config

def create_app():
    app = Flask(__name__)
    #app.config.from_object(app_config)

    from app import api_bp
    app.register_blueprint(api_bp, url_prefix='/storemanager/api/v1')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)