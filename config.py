from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
API_KEY = os.getenv('API_KEY_OPENAI')
SWID = os.getenv('SWID')
ESPN_2 = os.getenv('ESPN_2')
LEAGUE_ID = os.getenv('LEAGUE_ID')

class Config:
    """Basic configuration for the Flask app."""
    SECRET_KEY = "dev_secret_key"  # Change for production
    SQLALCHEMY_DATABASE_URI = "sqlite:///app.db"  # SQLite database
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable event notifications for performance

