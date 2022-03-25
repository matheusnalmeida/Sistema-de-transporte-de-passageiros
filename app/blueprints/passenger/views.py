from asyncore import read
from flask import Blueprint, jsonify, redirect, render_template, request, url_for
from flask_login import login_required
from app.models.entities.passenger import Passenger
from app.models.view.passenger_view_model import PassengerViewModel
from app.service.passenger_service import PassengerService
from app.utils import TEMPLATES_ROOT_PATH

passenger = Blueprint('passenger', __name__, template_folder=TEMPLATES_ROOT_PATH, url_prefix="/passenger")
passenger_service = PassengerService()

@passenger.route('/')
@login_required
def index():
    return render_template('passenger/index.html', passengers=passenger_service.get_all())

@passenger.route('/new', methods=['GET', 'POST'])
@login_required
def register():
    if request.method == 'GET':
        return render_template('passenger/register.html')
    else:
        new_passenger = Passenger(name = request.form['name'],
                        birth_date = request.form['birthdate'],
                        cpf = request.form['cpf'],
                        city = request.form['city'],
                        uf = request.form['uf'],
                        address = request.form['address'])        
        result = passenger_service.insert_passenger(new_passenger)

        if result.success:
            result.url = url_for('passenger.index')

        return jsonify(result.to_json())

@passenger.route("<int:id>/update", methods=['GET', 'POST'])
@login_required
def update(id):
    passenger = Passenger.query.get_or_404(id)
    if request.method == 'GET':
        return render_template('passenger/update.html', passenger=passenger)
    else:
        passenger_view = PassengerViewModel(
                        name = request.form["name"],
                        birth_date = request.form["birthdate"],
                        address= request.form["address"],
                        city = request.form["city"],
                        uf=request.form["uf"])

        result = passenger_service.update_passenger(passenger, passenger_view)

        if result.success:
            result.url = url_for('passenger.index')

        return jsonify(result.to_json())
        
@passenger.route("<int:id>/delete", methods=['GET'])
@login_required
def delete(id):
    passenger = Passenger.query.get_or_404(id)
    result = passenger_service.delete_passenger(passenger)        
    result.url = url_for('passenger.index')
    return jsonify(result.to_json())