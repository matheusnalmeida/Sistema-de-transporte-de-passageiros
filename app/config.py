import os
from app.utils import PROJECT_ROOT

class BaseConfig(object):
    PROJECT = "Sistema gerenciador de clientes"

    PROJECT_ROOT = PROJECT_ROOT

    DEBUG = False
    TESTING = False

    SECRET_KEY = '776699ca-a70f-11ec-b909-0242ac120002'

class DefaultConfig(BaseConfig):
    DEBUG = True