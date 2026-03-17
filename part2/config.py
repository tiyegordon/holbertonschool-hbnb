import os

#this is for application settings

class Config:

#SECRET KEY
#Flask uses this key behind the scenes for security purposes and to prevent a crash.

    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key')
    DEBUG = False


class DevelopmentConfig (Config):

#Shows detailed error message,auto restarts server when files are saved, turns app off when not in use

    DEBUG = True

#Available configurations for switching between test, dev, and prod using one word command.

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
 }
