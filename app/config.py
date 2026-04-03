import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'default-secret-key'
    DEBUG = False
    TESTING = False

class DevelopmentConfig(Config):
    DEBUG = True
    DATABASE_URI = os.environ.get('DEV_DATABASE_URI')

class ProductionConfig(Config):
    DATABASE_URI = os.environ.get('DATABASE_URI')
    # Additional production configurations can go here