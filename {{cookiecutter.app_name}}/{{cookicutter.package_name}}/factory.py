"""Factory module for the main package of {cookiecutter.app_name}

.. module:: views
    :platform: Unix
    :synopsis: Views for the main package.
.. moduleauthor:: {cookiecutter.author_name} <{cookiecutter.email}>
"""
from flask import Flask
from flask_bootstrap import Bootstrap
from .main import main as main_blueprint

bootstrap = Bootstrap()

def create_app():
    """Initialize the app."""
    app = Flask(__name__)
    # TODO Note that this key is just for development!
    app.config['SECRET_KEY'] = 'dev_key'
    app.register_blueprint(main_blueprint)
    bootstrap.init_app(app)
    return app

