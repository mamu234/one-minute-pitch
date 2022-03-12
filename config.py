import os

class Config:

   class Config:
        SECRET_KEY = os.environ.get('SECRET_KEY')
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://kk:admin@localhost/pitches'
        SQLALCHEMY_TRACK_MODIFICATIONS = False
   
   

class DevConfig(Config):
    DEBUG = True



config_options= {
    'development': DevConfig
}
