from app.utils import PROJECT_ROOT, DATA_ROOT_PATH

class BaseConfig(object):
    PROJECT = "Sistema gerenciador de clientes"
    PROJECT_ROOT = PROJECT_ROOT
    DEBUG = False
    TESTING = False
    STATIC_FOLDER="app/static"
    SECRET_KEY = '776699ca-a70f-11ec-b909-0242ac120002'

class DefaultConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + DATA_ROOT_PATH + '/database.db'