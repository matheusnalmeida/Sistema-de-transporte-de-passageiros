import re
from app.models.entities.transport import Transport
from datetime import datetime
from app.extensions import db
from app.models.entities.vehicle import Vehicle
from app.models.result import Result

class FinancialReportService:
    def __init__(self) -> None:
        pass
    
    def generate_report(self, begin_date = None, end_date = None) -> Result:
        result_transports_by_date = self.get_transports_by_date_interval(begin_date, end_date)
        
        if not result_transports_by_date.success:
            return result_transports_by_date

        result_aggregate_transports = self.get_transports_aggregate_by_vehicle_type(begin_date, end_date)

        if not result_aggregate_transports.success:
            return result_aggregate_transports
        
        return Result(success=True, data=(result_transports_by_date.data, result_aggregate_transports.data))

    def get_transports_by_date_interval(self, begin_date = None, end_date = None) -> Result:
        transports =  Transport.query

        result = self.apply_date_filter(transports, begin_date, end_date)
        if not result.success:
            return result
        transports = result.data

        transports =  transports.all()

        return Result(success=True, data=transports)

    def get_transports_aggregate_by_vehicle_type(self, begin_date = None, end_date = None) -> Result:
        transports_aggregate = db.session.query(
        Vehicle.type,
        db.func.sum(Transport.amount_charged_by_km).label('total_amount_charged'),
        db.func.count(Transport.id).label('total_transports')
        ).join(Transport.vehicle)

        result = self.apply_date_filter(transports_aggregate, begin_date, end_date)
        if not result.success:
            return result
        transports_aggregate = result.data

        transports_aggregate = transports_aggregate.group_by(Vehicle.type
        ).all()  

        dic_aggregate = lambda transports: {row.type: {
                                'total_amount_charged': round(row.total_amount_charged, 2),
                                'total_transports': row.total_transports}
                              for row in transports}
        
        dic_result_aggregate = dic_aggregate(transports_aggregate)

        total_amount_charged = 0
        total_transports = 0
        for type in dic_result_aggregate:
            total_amount_charged += dic_result_aggregate[type]['total_amount_charged']
            total_transports += dic_result_aggregate[type]['total_transports']
        
        dic_result_aggregate['total_amount_charged'] = round(total_amount_charged, 2)
        dic_result_aggregate['total_transports'] = round(total_transports, 2)

        return Result(success=True, data=dic_result_aggregate)

    
    def apply_date_filter(self, query, begin_date, end_date) -> Result:
        if begin_date and len(begin_date) > 0:
            try:
                begin_date = datetime.strptime(begin_date, '%Y-%m-%d').date()
            except ValueError:
                return Result(success=False, message='Data de inicio inválida!')
            query = query.filter(Transport.transport_date >= begin_date)

        if end_date != None and len(end_date) > 0:
            try:
                end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
            except ValueError:
                return Result(success=False, message='Data fim inválida!')
            query = query.filter(Transport.transport_date <= end_date)
        
        return Result(success=True, data=query)