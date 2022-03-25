from flask import Flask, render_template
from app.config import DefaultConfig
from app.extensions import db, bcrypt, login_manager
from app.models.entities.user import User

def create_app(config=None, app_name=None):
    if app_name is None:
        app_name = DefaultConfig.PROJECT

    app = Flask(app_name)
    configure_app(app, config)
    configure_hook(app)
    configure_blueprints(app)
    configure_extensions(app)
    configure_error_handlers(app)

    return app


def configure_app(app, config=None):
    app.config.from_object(DefaultConfig)
    
    if config:
        app.config.from_object(config)
    
    static_folder = app.config.get('STATIC_FOLDER')

    if static_folder:
        app.static_folder=static_folder

def configure_extensions(app):
    # flask-sqlalchemy
    db.init_app(app)
    with app.app_context():
        db.create_all()

    # bcrypt
    bcrypt.init_app(app)

    # flask-login
    login_manager.login_view = 'auth.login'
    #login_manager.refresh_view = 'auth.reauth'

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(id)

    login_manager.setup_app(app)

def configure_blueprints(appl):
    from app.blueprints.main import main
    from app.blueprints.auth import auth
    from app.blueprints.passenger import passenger

    for bp in [main, auth, passenger]:
        appl.register_blueprint(bp)

def configure_hook(app):
    @app.before_request
    def before_request():
        pass

def configure_error_handlers(app):
    @app.errorhandler(404)
    def page_not_found(error):
        return render_template("erros/404.html"), 404