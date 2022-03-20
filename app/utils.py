import os

PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

APP_ROOT = os.path.join(PROJECT_ROOT, 'app')

DATA_ROOT_PATH = os.path.join(APP_ROOT,  'data')

TEMPLATES_ROOT_PATH = os.path.join(APP_ROOT,  'templates')

INSTANCE_FOLDER_PATH = os.path.join('/tmp', 'instance')

ALLOWED_AVATAR_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
