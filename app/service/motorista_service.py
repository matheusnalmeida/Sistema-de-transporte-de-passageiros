from xml.etree.ElementTree import TreeBuilder

from jinja2 import pass_eval_context
from app.models.entities.motorista import Motorista
from app.models.result import Result
from app.extensions import db
from app.models.view.motorista_view_model import MotoristaViewModel

class MotoristaService:
    def __init__(self) -> None:
        pass

    def insert_motorista(self, motorista: Motorista) -> Result:
        result = motorista.is_valid()
        if not result.success:
            return result
        
        motoristaAlreadyExistsByName =  Motorista.query.filter_by(name=motorista.name).first()
        if motoristaAlreadyExistsByName:
           return Result(success=False, message="Ja existe um motorista cadastrado com o nome informado!")

        motoristaAlreadyExistsByCPF =  Motorista.query.filter_by(cpf=motorista.cpf).first()
        if motoristaAlreadyExistsByCPF:
           return Result(success=False, message="Ja existe um motorista cadastrado com o cpf informado!")
        
        db.session.add(motorista)
        db.session.commit()
        return Result(success= True, message= "Motorista registrado com sucesso!")
    
    def update_motorista(self, current_motorista: Motorista, motorista_view: MotoristaViewModel):
        current_motorista.fill_update(motorista_view)
        result = current_motorista.is_valid()

        if not result.success:
            return result

        db.session.commit()
        return Result(success=True, message="Motorista atualizado com sucesso!")

    def delete_motorista(self, motorista: Motorista):
        db.session.delete(motorista)
        db.session.commit()
        
        return Result(success=True, message="Motorista deletado com sucesso!")


    def get_all(self):
        return Motorista.query.all()