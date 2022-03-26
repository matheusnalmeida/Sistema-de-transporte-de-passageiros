from app.utils import cpf_formatter

class VehicleViewModel:
    def __init__(self, type = "", plate = "", brand = "", model = "", year = 0, capacity = 0, driver_cpf = "") -> None:
        self.type = type
        self.plate = plate
        self.brand = brand
        self.model = model
        self.year = int(year)
        self.capacity = int(capacity)
        self.driver_cpf = cpf_formatter(driver_cpf)
