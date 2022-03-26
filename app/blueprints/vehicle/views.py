from asyncore import read
from flask import Blueprint, jsonify, redirect, render_template, request, url_for
from flask_login import login_required
from app.models.entities.vehicle import Vehicle
from app.models.view.vehicle_view_model import VehicleViewModel
from app.service.vehicle_service import VehicleService
from app.utils import TEMPLATES_ROOT_PATH

vehicle = Blueprint('vehicle', __name__, template_folder=TEMPLATES_ROOT_PATH, url_prefix="/vehicle")
vehicle_service = VehicleService()

@vehicle.route('/')
@login_required
def index():
    return render_template('vehicle/index.html', vehicles=vehicle_service.get_all())

@vehicle.route('/new', methods=['GET', 'POST'])
@login_required
def register():
    if request.method == 'GET':
        return render_template('vehicle/register.html')
    else:
        new_vehicle = VehicleViewModel(type = request.form['tyoe'],
                        plate = request.form['plate'],
                        brand = request.form['brand'],
                        model = request.form['model'],
                        year = request.form['year'],
                        capacity = request.form['capacity'],
                        driver_cpf = request.form['driver_cpf'])        
        result = vehicle_service.insert_passenger(new_vehicle)

        if result.success:
            result.url = url_for('vehicle.index')

        return jsonify(result.to_json())

#@passenger.route("<int:id>/update", methods=['GET', 'POST'])
#@login_required
#def update(id):
#    passenger = Passenger.query.get_or_404(id)
#    if request.method == 'GET':
#        return render_template('passenger/update.html', passenger=passenger)
#    else:
#        passenger_view = PassengerViewModel(
#                        name = request.form["name"],
#                        birth_date = request.form["birthdate"],
#                        address= request.form["address"],
#                        city = request.form["city"],
#                        uf=request.form["uf"])
#
#        result = passenger_service.update_passenger(passenger, passenger_view)
#
#        if result.success:
#            result.url = url_for('passenger.index')
#
#        return jsonify(result.to_json())
#        
#@passenger.route("<int:id>/delete", methods=['GET'])
#@login_required
#def delete(id):
#    passenger = Passenger.query.get_or_404(id)
#    result = passenger_service.delete_passenger(passenger)        
#    result.url = url_for('passenger.index')
#    return jsonify(result.to_json())