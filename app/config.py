import os

class Config:
    """Base configuration class."""
    SECRET_KEY = os.environ.get('SECRET_KEY', 'your-default-secret-key')  # Use an environment variable or default
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # If you're using a database

class DevelopmentConfig(Config):
    """Configuration for development environment."""
    DEBUG = True
    ENV = 'development'

class TestingConfig(Config):
    """Configuration for testing environment."""
    TESTING = True
    DEBUG = True
    ENV = 'testing'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'  # In-memory database for tests

class ProductionConfig(Config):
    """Configuration for production environment."""
    DEBUG = False
    ENV = 'production'
    # For production, you would set a real database URI like:
    # SQLALCHEMY_DATABASE_URI = 'postgresql://user:password@localhost/mydatabase'
