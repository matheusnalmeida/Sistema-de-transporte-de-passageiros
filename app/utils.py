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

def valid_hour_format(hour: str):
    # HH:MM
    hour_match = re.fullmatch(r'^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$', hour)
    return hour_match and hour_match.group() == hour

def calculate_amount_charged(km_quantity):
    return round(0.40 * km_quantity, 2)

def valid_amount_charged(km_quantity, amount_charged):
    return round(0.40 * km_quantity, 2) == amount_charged