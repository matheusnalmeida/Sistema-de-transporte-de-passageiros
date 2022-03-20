from flask import Blueprint, render_template, request, jsonify
from app.utils import TEMPLATES_ROOT_PATH

auth = Blueprint('auth', __name__, template_folder=TEMPLATES_ROOT_PATH, url_prefix="/auth")

@auth.route('/login')
def login():
    if(request.method == 'GET'):
        return render_template('auth/login.html')
    else:
        response = user_service.login(request.form['usuario'], request.form['senha'])
        if response.success:
            response.url = url_for('index')
            session['logged_user'] = vars(response.data)

        return jsonify(response.to_json()) 


@auth.route('/logout')
def logout():
    return 'nice'

@auth.route('/register')
def register():
    return render_template('auth/register.html')

