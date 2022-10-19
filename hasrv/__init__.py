#!/bin/env python3

# Raspberry PI basic Home automation page using OOK  monitoring program RPI-RF


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from os import environ, path
from datetime import timedelta
import logging

hasrvdb=SQLAlchemy()



def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    app.config['REMEMBER_COOKIE_DURATION'] = timedelta(seconds=900)

    # Flat file DB because it's pretty basic, moving out of harms way though 
    app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////var/tmp/hasrv_io_state.sqlite3'
    app.config ['SQLALCHEMY_TRACK_MODIFCATIONS'] = False
    hasrvdb.init_app(app)  # Binds the driver to the datbase location


    with app.app_context():
        # Track URLs for app
        from .applogic import applogic as applogic_blueprint
        # Register the bluebprints to make dynamic HTML a little easier
        app.register_blueprint(applogic_blueprint)

        # app components initialized
        return app