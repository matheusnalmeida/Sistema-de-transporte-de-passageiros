from flask import Blueprint, redirect, render_template, request, jsonify, url_for
from flask_login import current_user, logout_user, login_required, login_user
from app.models.result import Result
from app.models.entities.user import User
from app.utils import TEMPLATES_ROOT_PATH
from app.service.user_service import UserService

auth = Blueprint('auth', __name__, template_folder=TEMPLATES_ROOT_PATH, url_prefix="/auth")
user_service = UserService()

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('auth/login.html')
    else:
        if current_user.is_authenticated:
            return jsonify(Result(success=True, url=url_for('main.index')).to_json())

        result = user_service.login(request.form['username'],
                                     request.form['password'])

        if result.success:
            result.url = url_for('main.index')
            
        return jsonify(result.to_json())

@auth.route('/logout')
@login_required
def logout():
    if current_user.is_authenticated:
        logout_user()
    return redirect(url_for('auth.login'))