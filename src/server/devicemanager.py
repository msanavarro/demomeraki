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

bp = Blueprint('devicemanager', __name__)

@bp.route('/v1/report/devicemanager', methods=['GET', 'POST', 'DELETE'])
def manage_devices():
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
                'INSERT INTO static_devices (macaddr, name) VALUES (?, ?)',
                (macaddr, name)
            )
            db.commit()
            return("Static device successfuly registered", 200)
    if request.method == 'GET':
        error = None
        db = get_db()
        cursor = db.cursor()
        cursor.execute(
            'SELECT * FROM static_devices'
        )
        rows = cursor.fetchall()
        data = []
        for row in rows:
            data.append({"macaddr":row['macaddr'], 
                         "name":row['name'], 
                         "registrationtime": row['registrationtime'].strftime('%Y-%m-%d %H:%M:%S'), 
                         "disconnectiontime": row['disconnectiontime'].strftime('%Y-%m-%d %H:%M:%S')
                         })
        return json.dumps(data)
        if error is not None:
            return (error, 400)

            
    if request.method == 'DELETE':
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
                'DELETE FROM static_devices WHERE macaddr = ? AND name = ?',
                (macaddr, name)
            )
            db.commit()
            return("Static device registry deleted", 200)

    return("Client successfuly registered", 200)

def disconnection_alarm():
    return
