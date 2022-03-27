from sqlalchemy import Column
from app.extensions import db
from app.models.entities.shared.person import Person
from app.models.result import Result
from datetime import datetime
from app.models.view.passenger_view_model import PassengerViewModel

class Passenger(Person):
    __tablename__ = 'passengers'

    id = Column(db.Integer, primary_key=True)
    city = Column(db.String(255), nullable=False)
    uf = Column(db.String(2), nullable=False)

    def is_valid(self) -> Result:
        if (
            not self.name or len(self.name) == 0 or
            not self.cpf or len(self.cpf) == 0 or
            not self.address or len(self.address) == 0 or
            not self.uf or len(self.address) == 0 or
            not self.city or len(self.city) == 0
        ):
            return Result(success= False,message= "Preencha todos os campos!")

        if len(self.uf) < 2 or len(self.uf) > 2:
            return Result(success= False,message= "O códigod a UF precisa de exatamente dois digitos!")

        if not self.cpf or len(self.cpf) < 11:
            return Result(success= False,message= "CPF inválido!")
        
        if not self.birth_date:
            return Result(success= False,message= "Data inválida!")
                
        if  datetime.now().date() < self.birth_date:
            return Result(success= False,message= "A data de nascimento não pode ser maior que a data atual!")

        return Result(success=True)            
    
    def fill_update(self, passenger: PassengerViewModel):
        self.name = passenger.name
        self._set_birthdate(passenger.birth_date)
        self.city = passenger.city
        self.uf = passenger.uf
        self.address = passenger.address