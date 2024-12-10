# Import the application factory function from the app package
from app import create_app

# Create an instance of the Flask application using the factory function
# This function initializes the app with all configurations and blueprints
app = create_app()

# Run the Flask application
# __name__ == "__main__" ensures this block runs only if the script is executed directly
# debug=True enables debug mode, providing detailed error pages and auto-reloading
if __name__ == "__main__":
    app.run(debug=True)
