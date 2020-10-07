'''
Created on 6 oct. 2020

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

bp = Blueprint('peoplemanager', __name__)

@bp.route('/v1/report/peoplemanager', methods=['GET', 'POST', 'DELETE'])
def manage_people():
    if request.method == 'POST':
        macaddr = request.json['macaddr']
        name = request.json['name']
        error = None

        if not macaddr or not name:
            error = 'Mac address and device name are required'

        if error is not None:
            return (error, 400)
        
        else:
            db = get_db()
            db.execute(
                'INSERT INTO people (macaddr, name) VALUES (?, ?)',
                (macaddr, name)
            )
            db.commit()
            return("Person successfuly registered", 200)
    if request.method == 'GET':
        error = None
        db = get_db()
        cursor = db.cursor()
        cursor.execute(
            'SELECT * FROM people'
        )
        rows = cursor.fetchall()
        data = []
        for row in rows:
            data.append({"macaddr":row['macaddr'], 
                         "name":row['name']
                         })
        return json.dumps(data)
        if error is not None:
            return (error, 400)

            
    if request.method == 'DELETE':
        macaddr = request.json['macaddr']
        name = request.json['name']
        error = None

        if not macaddr or not name:
            error = 'Mac address and person name are required'

        if error is not None:
            return (error, 400)
        
        else:
            db = get_db()
            db.execute(
                'DELETE FROM people  WHERE macaddr = ? AND  name = ?',
                (macaddr, name)
            )
            db.commit()
            return("Person registry deleted", 200)

    return("Server error", 500)

def visits_table_helper(locationdata):
    db = get_db()
    #  ESTE CICLO REVISA Y REGISTRA LAS LLEGADAS
    for value in locationdata["data"]["observations"] :
        macaddr = (value["clientMac"],)
        exists = db.execute("SELECT EXISTS(SELECT 1 FROM visits WHERE macaddr=?)", macaddr)
        if(exists.fetchone()[0]==0):
            db.execute(
                'INSERT INTO visits (macaddr, name, timesseen, averagestay)'
                    ' VALUES (?, ?, ?, ?)',
                    (value["clientMac"],"Cambiar nombre", 1, 0)
                )
            db.commit()
        else:
            # PENDIENTE CAMBIAR CONSULTAS POR UNA SOLA LECTURA QUE TOME TODO Y LO META EN UN DICCIONARIO
            lastarrivaltime = list(db.execute("SELECT lastarrivaltime FROM visits WHERE macaddr=?", macaddr).fetchone())[0]
            lastexittime = list(db.execute("SELECT lastexittime FROM visits WHERE macaddr=?", macaddr).fetchone())[0]
            timesseen = list(db.execute("SELECT timesSEEN FROM visits WHERE macaddr=?", macaddr).fetchone())[0]
            if(lastarrivaltime >= lastexittime):
                print('{} está en el edificio'.format(macaddr[0]))
            else:
                db.execute(
                    'UPDATE visits SET lastarrivaltime = CURRENT_TIMESTAMP WHERE macaddr = ?', 
                    (value["clientMac"],)
                    )
                db.commit()
                print('{} acaba de entrar al edificio'.format(macaddr))
    #  ESTE CICLO REVISA Y REGISTRA LAS SALIDAS
    cursor = db.cursor()
    cursor.execute(
        'SELECT * FROM visits'
    )
    rows = cursor.fetchall()
    dbdata = []
    for row in rows:
        macaddr = (row['macaddr'],)
        if (any(d['clientMac'] == row['macaddr'] for d in locationdata['data']['observations'])):
            print('{} sigue en el edificio'.format(row['macaddr']))
        else:
            lastarrivaltime = list(db.execute("SELECT lastarrivaltime FROM visits WHERE macaddr=?", macaddr).fetchone())[0]
            lastexittime = list(db.execute("SELECT CURRENT_TIMESTAMP AS ", macaddr).fetchone())[0]
            timesseen = list(db.execute("SELECT timesseen FROM visits WHERE macaddr=?", macaddr).fetchone())[0]
            averagestay = list(db.execute("SELECT averagestay FROM visits WHERE macaddr=?", macaddr).fetchone())[0]
            print(lastarrivaltime, lastexittime)
            newavgstay = (timesseen*averagestay +(lastexittime - lastarrivaltime).total_seconds())/(timesseen+1)
            db.execute(
                    'UPDATE visits SET lastexittime = CURRENT_TIMESTAMP, timesseen = ?, averagestay = ? WHERE macaddr = ?', 
                    (timesseen + 1, newavgstay, row['macaddr'])
                    )
            db.commit()
            print('{} salió del edificio'.format(row['macaddr']))
    return
