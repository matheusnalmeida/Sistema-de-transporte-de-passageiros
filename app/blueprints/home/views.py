from flask import Blueprint, render_template
from app.utils import TEMPLATES_ROOT_PATH

home = Blueprint('home', __name__, template_folder=TEMPLATES_ROOT_PATH)

@home.route('/')
def index():
    return render_template('home/index.html')