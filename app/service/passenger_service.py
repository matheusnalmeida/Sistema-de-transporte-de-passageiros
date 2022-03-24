from app.models.passenger import Passenger
from app.models.result import Result
from app.extensions import db

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
    
    def get_all(self):
        return Passenger.query.all()