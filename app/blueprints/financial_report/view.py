
from flask import Blueprint, jsonify, render_template, request
from flask_login import login_required
from app.constants import VEHICLE_TYPES
from app.service.financial_report_service import FinancialReportService
from app.utils import TEMPLATES_ROOT_PATH

financial_report = Blueprint('financial_report', __name__, template_folder=TEMPLATES_ROOT_PATH, url_prefix="/financial_report")
financial_report_service = FinancialReportService()

@financial_report.route('/', methods=['GET'])
@login_required
def index():
    result = financial_report_service.generate_report()
    transports_by_date, transports_aggregate = result.data

    return render_template('financial_report/index.html', 
                                      transports = transports_by_date,
                                      aggregate_transports = transports_aggregate,
                                      vehicle_types= VEHICLE_TYPES)

@financial_report.route('/search', methods=['GET'])
@login_required
def search():
    begin_date = request.args.get('transport-begin-date')
    end_date = request.args.get('transport-end-date')
    
    result = financial_report_service.generate_report(begin_date, end_date)

    if result.success:
        transports_by_date, transports_aggregate = result.data
        result.data = render_template('financial_report/report_content.html',
                                      transports = transports_by_date,
                                      aggregate_transports = transports_aggregate,
                                      vehicle_types= VEHICLE_TYPES)


    return jsonify(result.to_json())
