from sqlalchemy import Column
from app.extensions import db
from app.models.result import Result
from datetime import datetime
from app.models.view.transport_view_model import TransportViewModel

from app.utils import valid_amount_charged

class Transport(db.Model):
    __tablename__ = 'transports'

    id = Column(db.Integer, primary_key=True)
    vehicle_id = db.Column(db.Integer, db.ForeignKey('vehicles.id'), nullable=False)
    vehicle = db.relationship("Vehicle", backref="vehicle", uselist=False) 
    passenger_id = db.Column(db.Integer, db.ForeignKey('passengers.id'), nullable=False)
    passenger = db.relationship("Passenger", backref="passenger", uselist=False) 
    _transport_date = Column('transport_date', db.DateTime, nullable=False)
    transport_hour = Column(db.Integer, nullable=False)
    km_quantity = Column(db.Integer, nullable=False)
    amount_charged_by_km = Column(db.Float, nullable=False)

    def _get__transportdate(self):
        return self._transport_date
    def _set_transportdate(self, transport_date):
        self._transport_date = datetime.strptime(transport_date, '%Y-%m-%d').date()
    transport_date = db.synonym('_transport_date',
                    descriptor=property(_get__transportdate,
                                            _set_transportdate))

    def is_valid(self) -> Result:
        if (
            not self.vehicle_id or self.vehicle_id == 0 or
            not self.passenger_id or self.passenger_id == 0 or 
            not self.km_quantity or len(self.km_quantity) == 0 or
            not self.amount_charged_by_km or self.amount_charged_by_km == 0
        ):
            return Result(success= False,message= "Preencha todos os campos!")

        if not self.transport_date or not self.transport_hour:
            return Result(success= False,message= "Data inválida!")
                
        if  datetime.now().date() < self.transport_date:
            return Result(success= False,message= "A data do transporte não pode ser maior que a data atual!")

        if not valid_amount_charged(self.amount_charged_by_km):
            return Result(success= False,message= "O valor cobrado por km possui um valor inválido!")

        return Result(success=True)            
    
    def fill_update(self, transport: TransportViewModel):
        self.transport_date = transport.transport_date
        self.transport_hour = transport.transport_hour
        self.amount_charged_by_km = transport.amount_charged_by_km