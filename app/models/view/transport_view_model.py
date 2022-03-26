from app.utils import calculate_amount_charged

class TransportViewModel:
    def __init__(self, plate = "", cpf_passenger = "", transport_date = "", transport_hour = "", km_quantity = "") -> None:
        self.plate = plate
        self.cpf_passenger = cpf_passenger
        self.transport_date = transport_date
        self.transport_hour = transport_hour
        self.km_quantity = km_quantity
        self.amount_charged_by_km = calculate_amount_charged(self.km_quantity)