#!/bin/env python3
# Author(s): Doug Leece
# Version history:  Sept 11/2022 - Config file to avoid hardcoding settings in main file.  Make application more portable
#     
# Based on hackers & Slackers, using environment vars

from os import environ, path
from dotenv import load_dotenv

# Assuming it reads the input file from a path relative to where the app is being called from
basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


TESTING = True
DEBUG = True
FLASK_ENV = 'development'
SECRET_KEY = environ.get('SECRET_KEY')