import configparser
import os
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

# load the config from config path in system env
_cfg_path = os.getenv('PGAPP_CFG_PATH', '../config.ini')
_config = configparser.ConfigParser().read(_cfg_path)

# if there is no name then we are just bombing
app = Flask(_config['app.details']['name'])
app.config['SQLALCHEMY_DATABASE_URI'] = _config['app.details']['db_path']
db = SQLAlchemy(app)