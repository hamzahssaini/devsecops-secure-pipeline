from flask import Flask

def create_app():
    """
    Application factory for the Flask app.
    This structure is recommended for larger, production-ready applications.
    """
    app = Flask(__name__)
    
    # Initialize and register routes
    from .routes import init_routes
    init_routes(app)
    
    return app
