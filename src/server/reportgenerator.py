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

bp = Blueprint('reportgenerator', __name__)

@bp.route('/v1/report/general', methods=['GET'])
def generate_general_report():
    if request.method == 'GET':
        error = None
        db = get_db()
        cursor = db.cursor()
        name = None
        try:
            name = request.args['name']
            cursor.execute(
                'SELECT * FROM visits WHERE name = ?',
                (name,)
                )
        except:
            cursor.execute(
                'SELECT * FROM visits'
                )
        rows = cursor.fetchall()
        data = []
        for row in rows:
            data.append({"macaddr":row['macaddr'], 
                         "name":row['name'], 
                         "timesseen":row['timesseen'],
                         "maxstay":row["maxstay"],
                         "maxdate":row["maxdate"],
                         "minsstay":row["minstay"],
                         "mindate":row["mindate"],
                         "averagestay":row['averagestay']
                         })
        return json.dumps(data)
        if error is not None:
            return (error, 400)
    return("Server error", 500)

@bp.route('/v1/report/intradia', methods=['GET'])
def generate_slice_report():
    if request.method == 'GET':
        error = None
        db = get_db()
        cursor = db.cursor()
        try:
            date_hour = request.args['date_hour']
            cursor.execute(
                'SELECT * FROM slice WHERE date_hour = ?',
                (date_hour,)
                )
        except:
            cursor.execute(
                'SELECT * FROM slice'
                )
        rows = cursor.fetchall()
        data = []
        for row in rows:
            data.append({"date_hour":row['date_hour'], 
                         "floor0":row['floor0'], 
                         "floor1":row['floor1'],
                         "floor2":row['floor2'],
                         "floor3":row['floor3']
                         })
        return json.dumps(data)
        if error is not None:
            return (error, 400)
    return("Server error", 500)