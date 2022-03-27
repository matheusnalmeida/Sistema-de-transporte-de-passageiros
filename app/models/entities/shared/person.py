from datetime import datetime
from app.extensions import db
from app.utils import cpf_formatter
from sqlalchemy import Column
from sqlalchemy.ext.declarative import declared_attr

class Person(db.Model):
    __abstract__ = True

    name = Column(db.String(255), nullable=False, unique=True)
    _birth_date = Column('birth_date', db.DateTime, nullable=False)
    _cpf = Column('cpf', db.String(11), nullable = False, unique = True)
    address = Column(db.String(255), nullable=False)

    def _get_cpf(self):
        return self._cpf

    def _set_cpf(self, cpf: str):
        self._cpf = cpf_formatter(cpf)             
    
    @declared_attr
    def cpf(self):
        return db.synonym('_cpf',
                    descriptor=property(self._get_cpf,
                                            self._set_cpf))

    def _get_birthdate(self):
        return self._birth_date

    def _set_birthdate(self, birthdate):
        self._birth_date = datetime.strptime(birthdate, '%Y-%m-%d').date()
    
    @declared_attr
    def birth_date(self):
        return db.synonym('_birth_date',
                    descriptor=property(self._get_birthdate,
                                            self._set_birthdate))