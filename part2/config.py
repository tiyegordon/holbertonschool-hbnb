import os

##this is for application settings##

class Config:
    
    SECRET_KEY = os.getenv ('Secret_Keu', 'dev-secret-key')
    DEBUG = False

class DevelopmentConfig (Config):
    Debug = True

config = {
        'development': DevelopmentConfig,
        'default': DeveopmentConfig

