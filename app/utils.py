import os

PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

TEMPLATES_ROOT_PATH = os.path.join(PROJECT_ROOT, 'app',  'templates')

INSTANCE_FOLDER_PATH = os.path.join('/tmp', 'instance')

ALLOWED_AVATAR_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
