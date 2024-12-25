from flask import Flask
from flask_restful import Api
from app.routes import initialize_routes

def create_app():
    app = Flask(__name__)
    api = Api(app)
    
    # Initialize routes
    initialize_routes(api)
    
    return app
