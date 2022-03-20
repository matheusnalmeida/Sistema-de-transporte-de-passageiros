from flask import Blueprint, render_template
from app.utils import TEMPLATES_ROOT_PATH

main = Blueprint('main', __name__, template_folder=TEMPLATES_ROOT_PATH)

@main.route('/')
def index():
    return render_template('index.html')