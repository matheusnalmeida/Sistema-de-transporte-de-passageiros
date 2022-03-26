from xml.etree.ElementTree import TreeBuilder
from app.models.entities.driver import Driver
from app.models.result import Result
from app.extensions import db
from app.models.view.driver_view_model import DriverViewModel

class DriverService:
    def __init__(self) -> None:
        pass

    def insert_driver(self, driver: Driver) -> Result:
        result = driver.is_valid()
        if not result.success:
            return result
        
        driverAlreadyExistsByName =  Driver.query.filter_by(name=driver.name).first()
        if driverAlreadyExistsByName:
           return Result(success=False, message="Ja existe um motorista cadastrado com o nome informado!")

        driverAlreadyExistsByCPF =  Driver.query.filter_by(cpf=driver.cpf).first()
        if driverAlreadyExistsByCPF:
           return Result(success=False, message="Ja existe um motorista cadastrado com o cpf informado!")
        
        db.session.add(driver)
        db.session.commit()
        return Result(success= True, message= "Motorista registrado com sucesso!")
    
    def update_driver(self, current_driver: Driver, driver_view: DriverViewModel):
        current_driver.fill_update(driver_view)
        result = current_driver.is_valid()

        if not result.success:
            return result

        db.session.commit()
        return Result(success=True, message="Motorista atualizado com sucesso!")

    def delete_driver(self, driver: Driver):
        db.session.delete(driver)
        db.session.commit()
        
        return Result(success=True, message="Motorista deletado com sucesso!")


    def get_all(self):
        return Driver.query.all()