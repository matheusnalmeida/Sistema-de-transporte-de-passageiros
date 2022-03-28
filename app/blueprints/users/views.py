

from flask import Blueprint, jsonify, render_template, request, url_for
from flask_login import login_required
from app.models.entities.user import User
from app.models.view.user_view_model import UserViewModel
from app.service.user_service import UserService
from app.utils import TEMPLATES_ROOT_PATH


user = Blueprint('user', __name__, template_folder=TEMPLATES_ROOT_PATH, url_prefix="/user")
user_service = UserService()

@user.route('/')
@login_required
def index():
    return render_template('user/index.html', users=user_service.get_all_non_admin())

@user.route('/new', methods=['GET', 'POST'])
@login_required
def register():
    if request.method == 'GET':
        return render_template('user/register.html')
    else:
        newUser = User(name = request.form['name'],
                        birth_date = request.form['birthdate'],
                        cpf = request.form['cpf'],
                        login = request.form['login'],
                        password = request.form['password'],
                        address = request.form['address'])        
        result = user_service.insert_user(newUser)

        if result.success:
            result.url = url_for('user.index')

        return jsonify(result.to_json())

@user.route("<int:id>/update", methods=['GET', 'POST'])
@login_required
def update(id):
    user = User.query.get_or_404(id)
    if request.method == 'GET':
        return render_template('user/update.html', user=user)
    else:
        user_view = UserViewModel(
                        name = request.form["name"],
                        birth_date = request.form["birthdate"],
                        address=request.form["address"],
                        login=request.form["login"])

        result = user_service.update_user(user, user_view)

        if result.success:
            result.url = url_for('user.index')

        return jsonify(result.to_json())
        
@user.route("<int:id>/delete", methods=['GET'])
@login_required
def delete(id):
    user = User.query.get_or_404(id)
    result = user_service.delete_user(user) 
    if result.success:      
        result.url = url_for('user.index')
    return jsonify(result.to_json())