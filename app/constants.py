from ctypes import addressof

from flask_login import login_fresh
from app.models.entities.user import User
from datetime import datetime

VEHICLE_TYPES = {
    'Carro': 'Carro',
    'Onibus': 'Onibus',
    'Van': 'Van',
}

ADMIN_DEFAULT_USER = User(
    name = "Sr. Francisco",
    birth_date = '2022-03-27',
    cpf = '0',
    address = 'default',
    login = 'admin',
    password = 'admin',
    is_admin = True
)