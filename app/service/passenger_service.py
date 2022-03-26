from app.models.entities.passenger import Passenger
from app.models.entities.transport import Transport
from app.models.result import Result
from app.extensions import db
from app.models.view.passenger_view_model import PassengerViewModel

class PassengerService:
    def __init__(self) -> None:
        pass

    def insert_passenger(self, passenger: Passenger) -> Result:
        result = passenger.is_valid()
        if not result.success:
            return result
        
        passengerAlreadyExistsByName =  Passenger.query.filter_by(name=passenger.name).first()
        if passengerAlreadyExistsByName:
           return Result(success=False, message="Ja existe um passageiro cadastrado com o nome informado!")

        passengerAlreadyExistsByCPF =  Passenger.query.filter_by(cpf=passenger.cpf).first()
        if passengerAlreadyExistsByCPF:
           return Result(success=False, message="Ja existe um passageiro cadastrado com o cpf informado!")
        
        db.session.add(passenger)
        db.session.commit()
        return Result(success= True, message= "Passageiro registrado com sucesso!")
    
    def update_passenger(self, current_passenger: Passenger, passenger_view: PassengerViewModel):
        current_passenger.fill_update(passenger_view)
        result = current_passenger.is_valid()

        if not result.success:
            return result

        db.session.commit()
        return Result(success=True, message="Passageiro atualizado com sucesso!")

    def delete_passenger(self, passenger: Passenger):
        transport = Transport.query.filter_by(passenger_id=passenger.id).first()
        if transport != None:
            return Result(success=False, message='''Existem registros de transportes cadastrados com esse passageiro!''')
        db.session.delete(passenger)
        db.session.commit()
        
        return Result(success=True, message="Passageiro deletado com sucesso!")


    def get_all(self):
        return Passenger.query.all()