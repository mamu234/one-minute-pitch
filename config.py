import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://carolyne:123@localhost/pitches'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
   
   

class DevConfig(Config):
    DEBUG = True

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    if SQLALCHEMY_DATABASE_URI and SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://", 1)
    pass

config_options= {
    'development': DevConfig,
    'production': ProdConfig

}
