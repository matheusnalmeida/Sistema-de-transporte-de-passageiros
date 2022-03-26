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
        new_vehicle = VehicleViewModel(type = request.form['type'],
                        plate = request.form['plate'],
                        brand = request.form['brand'],
                        model = request.form['model'],
                        year = request.form['year'],
                        capacity = request.form['capacity'],
                        driver_cpf = request.form['driver-cpf'])        
        result = vehicle_service.insert_vehicle(new_vehicle)

        if result.success:
            result.url = url_for('vehicle.index')

        return jsonify(result.to_json())

@vehicle.route("<int:id>/update", methods=['GET', 'POST'])
@login_required
def update(id):
    vehicle = Vehicle.query.get_or_404(id)
    if request.method == 'GET':
        return render_template('vehicle/update.html', vehicle=vehicle)
    else:
        vehicle_view = VehicleViewModel(
                        type = request.form['type'],
                        brand = request.form['brand'],
                        model = request.form['model'],
                        year = request.form['year'],
                        capacity = request.form['capacity'],
                        driver_cpf = request.form['driver-cpf'])

        result = vehicle_service.update_vehicle(vehicle, vehicle_view)

        if result.success:
            result.url = url_for('vehicle.index')

        return jsonify(result.to_json())
        
@vehicle.route("<int:id>/delete", methods=['GET'])
@login_required
def delete(id):
    vehicle = Vehicle.query.get_or_404(id)
    result = vehicle_service.delete_vehicle(vehicle)        
    result.url = url_for('vehicle.index')
    return jsonify(result.to_json())