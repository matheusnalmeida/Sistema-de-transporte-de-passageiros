from multiprocessing.sharedctypes import Value
from types import TracebackType
from unittest import result
from app.models.entities.transport import Transport
from datetime import datetime

from app.models.result import Result

class FinancialReportService:
    def __init__(self) -> None:
        pass
    
    def get_report_data(self, begin_date = None, end_date = None) -> Result:
        transports =  Transport.query

        if begin_date and len(begin_date) > 0:
            try:
                begin_date = datetime.strptime(begin_date, '%Y-%m-%d').date()
            except ValueError:
                return Result(success=False, message='Data de inicio inválida!')
            transports = transports.filter(Transport.transport_date >= begin_date)

        if end_date != None and len(end_date) > 0:
            try:
                end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
            except ValueError:
                return Result(success=False, message='Data fim inválida!')
            transports = transports.filter(Transport.transport_date <= end_date)

        transports =  transports.all()

        return Result(success=True, data=transports)
