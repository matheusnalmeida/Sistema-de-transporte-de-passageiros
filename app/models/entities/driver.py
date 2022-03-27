from sqlalchemy import Column
from app.extensions import db
from app.models.entities.shared.person import Person
from app.models.result import Result
from datetime import datetime
from app.models.view.driver_view_model import DriverViewModel

class Driver(Person):
    __tablename__ = 'drivers'

    id = Column(db.Integer, primary_key=True)

    def is_valid(self) -> Result:
        if (
            not self.name or len(self.name) == 0 or
            not self.cpf or len(self.cpf) == 0 or
            not self.address or len(self.address) == 0
        ):
            return Result(success= False,message= "Preencha todos os campos!")

        if not self.cpf or len(self.cpf) < 11:
            return Result(success= False,message= "CPF inválido!")
        
        if not self.birth_date:
            return Result(success= False,message= "Data de nascimento inválida!")
                
        if  datetime.now().date() < self.birth_date:
            return Result(success= False,message= "A data de nascimento não pode ser maior que a data atual!")

        return Result(success=True)            
    
    def fill_update(self, driver: DriverViewModel):
        self.name = driver.name
        self._set_birthdate(driver.birth_date)
        self.address = driver.address