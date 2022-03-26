from app.models.entities.passenger import Passenger
from app.models.entities.transport import Transport
from app.models.entities.vehicle import Vehicle
from app.models.result import Result
from app.models.view.transport_view_model import TransportViewModel
from app.extensions import db

class TransportService:
    def __init__(self) -> None:
        pass

    def insert_transport(self, transport: TransportViewModel) -> Result:
        new_transport = Transport(
            transport_date = transport.transport_date,
            transport_hour = transport.transport_hour,
            km_quantity = transport.km_quantity,
            amount_charged_by_km = transport.amount_charged_by_km
        )

        result_vehicle = self.__validate_vehicle_exists(transport.plate)
        if not result_vehicle.success:
           return result_vehicle
        new_transport.vehicle_id = result_vehicle.data.id

        result_passenger = self.__validate_passenger_exists(transport.cpf_passenger)
        if not result_passenger.success:
           return result_passenger
        new_transport.passenger_id = result_passenger.data.id

        result = new_transport.is_valid()
        if not result.success:
            return result

        db.session.add(new_transport)
        db.session.commit()
        return Result(success= True, message= "Registro de transporte cadastrado com sucesso!")
    
    def update_transport(self, current_transport: Transport, transport_view: TransportViewModel):
        current_transport.fill_update(transport_view)

        result_vehicle = self.__validate_vehicle_exists(transport_view.plate)
        if not result_vehicle.success:
           return result_vehicle
        current_transport.vehicle_id = result_vehicle.data.id

        result_passenger = self.__validate_passenger_exists(transport_view.cpf_passenger)
        if not result_passenger.success:
           return result_passenger
        current_transport.passenger_id = result_passenger.data.id

        result = current_transport.is_valid()

        if not result.success:
            return result

        db.session.commit()
        return Result(success=True, message="Registro de transporte atualizado com sucesso!")

    def delete_transport(self, transport: Transport):
        db.session.delete(transport)
        db.session.commit()
        
        return Result(success=True, message="Registro de transporte deletado com sucesso!")

    def get_all(self): 
        return Transport.query.all()

    def __validate_vehicle_exists(self, vehicle_plate: str) -> Result:
        vehicle = Vehicle.query.filter_by(plate=vehicle_plate).first()

        if vehicle == None:
           return Result(success=False, message="Não existe veiculo com a placa informada!")
        
        return Result(success=True, data=vehicle)

    def __validate_passenger_exists(self, passenger_cpf: str) -> Result:
        passenger = Passenger.query.filter_by(cpf=passenger_cpf).first()

        if passenger == None:
           return Result(success=False, message="Não existe passageiro com o cpf informado!")
        
        return Result(success=True, data=passenger)