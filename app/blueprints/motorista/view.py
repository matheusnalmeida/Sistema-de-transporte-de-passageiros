from asyncore import read
from flask import Blueprint, jsonify, redirect, render_template, request, url_for
from flask_login import login_required
from app.models.entities.motorista import Motorista 
from app.models.view.motorista_view_model import MotoristaViewModel
from app.service.motorista_service import MotoristaService
from app.utils import TEMPLATES_ROOT_PATH

motorista = Blueprint('motorista', __name__, template_folder=TEMPLATES_ROOT_PATH, url_prefix="/motorista")
motorista_service = MotoristaService()

@motorista.route('/')
@login_required
def index():
    return render_template('motorista/index.html', motoristas=motorista_service.get_all())

@motorista.route('/new', methods=['GET', 'POST'])
@login_required
def register():
    if request.method == 'GET':
        return render_template('motorista/register.html')
    else:
        new_motorista = Motorista(name = request.form['name'],
                        birth_date = request.form['birthdate'],
                        cpf = request.form['cpf'],
                        city = request.form['city'],
                        uf = request.form['uf'],
                        address = request.form['address'])        
        result = motorista_service.insert_motorista(new_motorista)

        if result.success:
            result.url = url_for('motorista.index')

        return jsonify(result.to_json())

@motorista.route("<int:id>/update", methods=['GET', 'POST'])
@login_required
def update(id):
    motorista = Motorista.query.get_or_404(id)
    if request.method == 'GET':
        return render_template('motorista/update.html', motorista=motorista)
    else:
        passenger_view = MotoristaViewModel(
                        name = request.form["name"],
                        birth_date = request.form["birthdate"],
                        address= request.form["address"],
                        city = request.form["city"],
                        uf=request.form["uf"])

        result = motorista_service.update_passenger(motorista, passenger_view)

        if result.success:
            result.url = url_for('motorista.index')

        return jsonify(result.to_json())
        
@motorista.route("<int:id>/delete", methods=['GET'])
@login_required
def delete(id):
    motorista = Motorista.query.get_or_404(id)
    result = motorista_service.delete_passenger(motorista)        
    result.url = url_for('motorista.index')
    return jsonify(result.to_json())