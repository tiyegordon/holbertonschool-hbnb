import os
from datetime import timedelta

#this is for application settings

class Config:
    #SECRET KEY
    #Flask uses this key behind the scenes for security purposes and to prevent a crash.
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key')
    DEBUG = False
    
    # JWT Configuration
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'jwt-secret-key')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
    JWT_HEADER_TYPE = ''  # Uncomment for Swagger (raw token), comment out for Postman (Bearer prefix)
    
    # Database Configuration
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///hbnb.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig (Config):
    #Shows detailed error message,auto restarts server when files are saved, turns app off when not in use
    DEBUG = True


class ProductionConfig (Config):
    DEBUG = False
    # Use environment variable for production database (MySQL)
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'mysql://user:password@localhost/hbnb_prod')

#Available configurations for switching between test, dev, and prod using one word command

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}




