from flask import Flask





def create_app(config_class="config.Config",instance_relative_config=True):
    """
    Factory function to create a Flask application instance.
    """
    # Create the Flask app instance
    app = Flask(__name__)
    
    # Load default configuration from root config.py
    app.config.from_object('config.Config')  
    
    # Load sensitive configuration from instance/config.py
    app.config.from_pyfile('config.py', silent=True)  
    
    
    # Register blueprints
    from app.routes import main_bp
    app.register_blueprint(main_bp)
    
    return app

