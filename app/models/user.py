from sqlalchemy import Column
from flask_login import UserMixin
from app.extensions import db, bcrypt

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = Column(db.Integer, primary_key=True)
    name = Column(db.String(255), nullable=False, unique=True)
    birth_date = Column(db.DateTime, nullable=False)
    cpf = Column(db.String(11), nullable = False, unique = True)
    login = Column(db.String(255), nullable=False, unique=True)
    _password = Column('password', db.String(200), nullable=False)

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