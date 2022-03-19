import os

class BaseConfig(object):
    PROJECT = "Sistema gerenciador de clientes"

    PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

    DEBUG = False
    TESTING = False

    SECRET_KEY = '776699ca-a70f-11ec-b909-0242ac120002'

class DefaultConfig(BaseConfig):
    DEBUG = True