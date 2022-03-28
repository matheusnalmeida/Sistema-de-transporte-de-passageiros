from sqlalchemy import Column
from flask_login import UserMixin
from app.extensions import db, bcrypt
from app.models.entities.shared.person import Person
from app.models.result import Result
from datetime import datetime

from app.models.view.user_view_model import UserViewModel

class User(Person, UserMixin):
    __tablename__ = 'users'

    id = Column(db.Integer, primary_key=True)
    login = Column(db.String(255), nullable=False, unique=True)
    _password = Column('password', db.String(200), nullable=False)
    is_admin = db.Column(db.Boolean, default=False, nullable=False)

    def _get_password(self):
        return self._password
    def _set_password(self, password):
        self._password = bcrypt.generate_password_hash(password)
    password = db.synonym('_password',
                          descriptor=property(_get_password,
                                              _set_password))
                                            
    def check_password(self, password):
        if self.password is None:
            return False
        return bcrypt.check_password_hash(self.password, password)

    def is_valid(self) -> Result:
        if (
            not self.name or len(self.name) == 0 or
            not self.cpf or len(self.cpf) == 0 or
            not self.login or len(self.login) == 0 or
            not self.password or len(self.password) == 0 or
            not self.address or len(self.address) == 0 
        ):
            return Result(success= False,message= "Preencha todos os campos!")

        if not self.cpf or len(self.cpf) < 11:
            return Result(success= False,message= "CPF inválido!")
        
        if not self.birth_date:
            return Result(success= False,message= "Data inválida!")
                
        if  datetime.now().date() < self.birth_date:
            return Result(success= False,message= "A data de nascimento não pode ser maior que a data atual!")

        return Result(success=True)            

    def fill_update(self, user: UserViewModel):
        self.name = user.name
        self.birth_date = user.birth_date
        self.address = user.address
        self.login = user.login