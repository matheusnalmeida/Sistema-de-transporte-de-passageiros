from sqlalchemy import Column
from app.extensions import db
from app.models.result import Result
from app.models.view.vehicle_view_model import VehicleViewModel

class Vehicle(db.Model):
    __tablename__ = 'vehicles'

    id = Column(db.Integer, primary_key=True)
    type = Column(db.String(20), nullable = False, unique = True)
    plate = Column(db.String(7), nullable=False)
    brand = Column(db.String(255), nullable=False)
    model = Column(db.String(255), nullable=False)
    year = Column(db.Integer, nullable=False)
    capacity = Column(db.Integer, nullable=False)
    driver_id = db.Column(db.Integer, db.ForeignKey('drivers.id'), nullable=False)
    driver = db.relationship("Driver", backref="driver", uselist=False) 

    def is_valid(self) -> Result:
        if (
            not self.type or len(self.type) == 0 or
            not self.plate or len(self.plate) == 0 or
            not self.brand or len(self.brand) == 0 or
            not self.model or len(self.model) == 0 or
            not self.year or self.year == 0 or
            not self.capacity or
            not self.driver_id or self.driver_id == 0
        ):
            return Result(success= False,message= "Preencha todos os campos!")

        if self.capacity <= 0:
            return Result(success= False,message= "A capacidade precisa ser maior que zero!")

        if self.year < 1900:
            return Result(success= False,message= "O ano do veiculo precisa ser maior que 1900!")

        return Result(success=True)            
    
    def fill_update(self, vehicle: VehicleViewModel):
        self.type = vehicle.type
        self.brand = vehicle.brand
        self.model = vehicle.model
        self.year = vehicle.year
        self.capacity = vehicle.capacity