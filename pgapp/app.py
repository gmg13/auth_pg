import configparser
import os
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

# load the config from config path in system env
_cfg_path = os.getenv('PGAPP_CFG_PATH', '../config.ini')
_config = configparser.ConfigParser().read(_cfg_path)

# if there is no name then we are just bombing

import os
from flask import Flask
from .models import db
from .routes import bp


def create_app(c=_config):
    cfgapp = c['app']

    # create the app
    app = Flask(cfgapp['name'])

    # initialize the required config
    app.config['SQLALCHEMY_DATABASE_URI'] = cfgapp['db_path']
    app.config['CLIENT_ID'] = c['auth']

    # load default configuration
    app.config.from_object('website.settings')

    # load environment configuration
    if 'WEBSITE_CONF' in os.environ:
        app.config.from_envvar('WEBSITE_CONF')

    # load app specified configuration
    if c is not None:
        if isinstance(c, dict):
            app.config.update(c)
        elif c.endswith('.py'):
            app.config.from_pyfile(c)

    setup_app(app)
    return app


def setup_app(app):
    # Create tables if they do not exist already
    @app.before_first_request
    def create_tables():
        db.create_all()

    db.init_app(app)
    app.register_blueprint(bp, url_prefix='')
