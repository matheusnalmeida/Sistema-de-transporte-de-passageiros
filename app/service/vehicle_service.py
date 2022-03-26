from app.models.entities.vehicle import Vehicle
from app.models.result import Result
from app.models.view.vehicle_view_model import VehicleViewModel
from app.extensions import db

class VehicleService:
    def __init__(self) -> None:
        pass

    def insert_vehicle(self, vehicle: VehicleViewModel) -> Result:
        vehicle = Vehicle(
            type = vehicle.type,
            plate = vehicle.plate,
            brand = vehicle.brand,
            model = vehicle.model,
            year = vehicle.year,
            capacity = vehicle.capacity
        )
        # TODO Validação de passageiro existe

        result = vehicle.is_valid()
        if not result.success:
            return result
        
        vehicleAlreadyExistsByPlate =  Vehicle.query.filter_by(plate=vehicle.plate).first()
        if vehicleAlreadyExistsByPlate:
           return Result(success=False, message="Ja existe um veiculo com a placa informada!")

        db.session.add(vehicle)
        db.session.commit()
        return Result(success= True, message= "Veiculo cadastrado com sucesso!")
    
    def update_vehicle(self, current_vehicle: Vehicle, vehicle_view: VehicleViewModel):
        current_vehicle.fill_update(vehicle_view)
        result = current_vehicle.is_valid()

        if not result.success:
            return result

        db.session.commit()
        return Result(success=True, message="Veiculo atualizado com sucesso!")

    def delete_vehicle(self, vehicle: Vehicle):
        db.session.delete(vehicle)
        db.session.commit()
        
        return Result(success=True, message="Veiculo deletado com sucesso!")

    def get_all(self):
        return Vehicle.query.all()