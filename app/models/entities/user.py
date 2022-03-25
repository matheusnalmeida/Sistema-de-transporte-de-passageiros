from sqlalchemy import Column
from flask_login import UserMixin
from app.extensions import db, bcrypt
from app.models.result import Result
from datetime import datetime

from app.utils import cpf_formatter

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = Column(db.Integer, primary_key=True)
    name = Column(db.String(255), nullable=False, unique=True)
    _birth_date = Column('birth_date', db.DateTime, nullable=False)
    _cpf = Column('cpf', db.String(11), nullable = False, unique = True)
    login = Column(db.String(255), nullable=False, unique=True)
    _password = Column('password', db.String(200), nullable=False)
    address = Column(db.String(255), nullable=False)

    def _get_cpf(self):
        return self._cpf
    def _set_cpf(self, cpf: str):
        self._cpf = cpf_formatter(cpf)             
    cpf = db.synonym('_cpf',
                    descriptor=property(_get_cpf,
                                            _set_cpf))

    def _get_birthdate(self):
        return self._birth_date
    def _set_birthdate(self, birthdate):
        self._birth_date = datetime.strptime(birthdate, '%Y-%m-%d').date()
    birth_date = db.synonym('_birth_date',
                    descriptor=property(_get_birthdate,
                                            _set_birthdate))

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