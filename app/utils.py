import os
import re

PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

APP_ROOT = os.path.join(PROJECT_ROOT, 'app')

DATA_ROOT_PATH = os.path.join(APP_ROOT,  'data')

TEMPLATES_ROOT_PATH = os.path.join(APP_ROOT,  'templates')

INSTANCE_FOLDER_PATH = os.path.join('/tmp', 'instance')

ALLOWED_AVATAR_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])


def cpf_formatter(cpf :str):
    if cpf:
        cpf = re.sub('[\.|-]', '', cpf)
        cpf_digits = re.findall(r'\d+', cpf)    
        if len(cpf_digits) > 0:      
            return cpf_digits[0]  

def calculate_amount_charged(km_quantity):
    return 0.40 * km_quantity

def valid_amount_charged(km_quantity, amount_charged):
    return 0.40 * km_quantity == amount_charged