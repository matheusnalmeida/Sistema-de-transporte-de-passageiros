from flask import Blueprint, jsonify, render_template, request, url_for
from flask_login import login_required
from app.models.entities.transport import Transport
from app.models.view.transport_view_model import TransportViewModel
from app.service.transport_service import TransportService
from app.utils import TEMPLATES_ROOT_PATH

transport = Blueprint('transport', __name__, template_folder=TEMPLATES_ROOT_PATH, url_prefix="/transport")
transport_service = TransportService()

@transport.route('/')
@login_required
def index():
    return render_template('transport/index.html', transports=transport_service.get_all())

@transport.route('/new', methods=['GET', 'POST'])
@login_required
def register():
    if request.method == 'GET':
        return render_template('transports/register.html')
    else:
        # TODO FILL TRANSPORT VIEW MODEL
        new_transport = TransportViewModel()        
        result = transport_service.insert_transport(new_transport)

        if result.success:
            result.url = url_for('transport.index')

        return jsonify(result.to_json())

@transport.route("<int:id>/update", methods=['GET', 'POST'])
@login_required
def update(id):
    transport = Transport.query.get_or_404(id)
    if request.method == 'GET':
        return render_template('transport/update.html', transport=transport)
    else:
        # TODO FILL TRANSPORT VIEW MODEL
        transport_view = TransportViewModel()

        result = transport_service.update_transport(transport, transport_view)

        if result.success:
            result.url = url_for('transport.index')

        return jsonify(result.to_json())
        
@transport.route("<int:id>/delete", methods=['GET'])
@login_required
def delete(id):
    transport = Transport.query.get_or_404(id)
    result = transport_service.delete_transport(transport)        
    result.url = url_for('transport.index')
    return jsonify(result.to_json())