'''
Created on 7 oct. 2020

@author: msanavarro
'''
# Libraries
from pprint import pprint
from flask import Flask
from flask import Blueprint
from flask import json
from flask import request
from flask import render_template
from flask import current_app, g
import sys, getopt
import json
from server.db import get_db
import requests
import datetime

def slice_table_helper(locationdata):
    db = get_db()
    date_hour = datetime.datetime.now().strftime("%Y-%m-%d %H")
    exists = db.execute("SELECT EXISTS(SELECT 1 FROM slice WHERE date_hour=?)", (date_hour,))
    if(exists.fetchone()[0]==0):
        db.execute(
                'INSERT INTO slice (date_hour)'
                    ' VALUES (?)',
                    (date_hour,)
                )
        db.commit()
    
    print("{} tiene {} dispositivos".format(locationdata["data"]["apFloors"][0], len(locationdata['data']['observations'])))
    print(locationdata["data"]["apFloors"][0] == "Planta Baja")       
    if (locationdata["data"]["apFloors"][0] == "Planta Baja"):
        db.execute(
                'UPDATE slice SET floor0 = ? WHERE date_hour = ?',
                    (len(locationdata['data']['observations']),date_hour)
                )
        db.commit()
    elif (locationdata["data"]["apFloors"][0] == "Piso 1"):
        db.execute(
                'UPDATE slice SET floor1 = ? WHERE date_hour = ?',
                    (len(locationdata['data']['observations']),date_hour)
                )
        db.commit()
    elif (locationdata["data"]["apFloors"][0] == "Piso 2"):
        db.execute(
                'UPDATE slice SET floor2 = ? WHERE date_hour = ?',
                    (len(locationdata['data']['observations']),date_hour)
                )
        db.commit()
    elif (locationdata["data"]["apFloors"][0] == "Piso 3"):
        db.execute(
                'UPDATE slice SET floor3 = ? WHERE date_hour = ?',
                    (len(locationdata['data']['observations']),date_hour)
                )
        db.commit()
    else:
        print("No esta registrado este piso")
    
    return