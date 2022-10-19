#!/bin/env python3

#from flask_sqlalchemy import SQLAlchemy
from . import hasrvdb

#hasrvdb=SQLAlchemy()


class hasrvstate(hasrvdb.Model):
    __tablename__ = 'iostate'
    id = hasrvdb.Column(hasrvdb.Integer, primary_key=True)
    ioname = hasrvdb.Column(hasrvdb.String(32), index=False,unique=True,nullable=False)
    iodesc = hasrvdb.Column(hasrvdb.String(643), index=False,unique=False,nullable=True)
    iostate = hasrvdb.Column(hasrvdb.Integer, index=False,unique=False,nullable=False)

    # You need one function that returns some kind of string, return an array of all records
    def __repr__(self):
        # using format string to get around the inability to subscript
        return  'IOName:{},IOdescription:{},IOstate:{}'.format(self.ioname,self.iodesc,self.iostate)

