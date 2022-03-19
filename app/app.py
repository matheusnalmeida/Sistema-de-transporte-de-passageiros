import os
from flask import Flask, render_template, Blueprint
from app.config import DefaultConfig

def create_app(config=None, app_name=None):
    if app_name is None:
        app_name = DefaultConfig.PROJECT

    app = Flask(app_name)
    configure_app(app, config)
    configure_hook(app)
    configure_blueprints(app)
    configure_error_handlers(app)

    return app


def configure_app(app, config=None):
    app.config.from_object(DefaultConfig)
    
    if config:
        app.config.from_object(config)


def configure_blueprints(appl):
    from app.blueprints.home import home

    for bp in [home]:
        appl.register_blueprint(bp)

def configure_hook(app):

    @app.before_request
    def before_request():
        pass

def configure_error_handlers(app):
    @app.errorhandler(404)
    def page_not_found(error):
        return render_template("erros/404.html"), 404