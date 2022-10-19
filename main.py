#!/bin/env python3

# Raspberry PI basic Home automation page using OOK  monitoring program RPI-RF 
# 
# Use this to confirm your Flask installation is working correctly
#  
# Remove once you get things working with a more advanced application
# export FLASK_APP=main.py
# export FLASK_ENV=development
# flask run  -h 0.0.0.0  ( defaults tpo port 5000)


from flask import Flask

hwapp = Flask(__name__)

@hwapp.route('/')
def index():
    return 'Home Automation Server (HAS) default page'