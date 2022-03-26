from flask import Blueprint, jsonify, render_template, request, url_for
from flask_login import login_required
from app.models.entities.driver import Driver 
from app.models.view.driver_view_model import DriverViewModel
from app.service.driver_service import DriverService
from app.utils import TEMPLATES_ROOT_PATH

driver = Blueprint('driver', __name__, template_folder=TEMPLATES_ROOT_PATH, url_prefix="/driver")
driver_service = DriverService()

@driver.route('/')
@login_required
def index():
    return render_template('driver/index.html', drivers=driver_service.get_all())

@driver.route('/new', methods=['GET', 'POST'])
@login_required
def register():
    if request.method == 'GET':
        return render_template('driver/register.html')
    else:
        new_driver = Driver(name = request.form['name'],
                        birth_date = request.form['birthdate'],
                        cpf = request.form['cpf'],
                        address = request.form['address'])        
        result = driver_service.insert_driver(new_driver)

        if result.success:
            result.url = url_for('driver.index')

        return jsonify(result.to_json())

@driver.route("<int:id>/update", methods=['GET', 'POST'])
@login_required
def update(id):
    driver = Driver.query.get_or_404(id)
    if request.method == 'GET':
        return render_template('driver/update.html', motorista=driver)
    else:
        driver_view = DriverViewModel(
                        name = request.form["name"],
                        birth_date = request.form["birthdate"],
                        address= request.form["address"])

        result = driver_service.update_driver(driver, driver_view)

        if result.success:
            result.url = url_for('driver.index')

        return jsonify(result.to_json())
        
@driver.route("<int:id>/delete", methods=['GET'])
@login_required
def delete(id):
    motorista = Driver.query.get_or_404(id)
    result = driver_service.delete_driver(motorista)        
    result.url = url_for('driver.index')
    return jsonify(result.to_json())