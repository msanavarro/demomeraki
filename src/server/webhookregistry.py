'''
Created on 5 oct. 2020

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

bp = Blueprint('webhookregistry', __name__)

@bp.route('/v1/report/webhookregistry', methods=('POST', 'DELETE'))
def register_whClient():
    if request.method == 'POST':
        clientUrl = request.json['clientUrl']
        error = None

        if not clientUrl:
            error = 'Webhook client url required'

        if error is not None:
            return (error, 400)
        
        else:
            db = get_db()
            db.execute(
                'INSERT INTO webhook_clients (url) VALUES (?)',
                (clientUrl,)
            )
            db.commit()
    if request.method == 'DELETE':
        clientUrl = request.json['clientUrl']
        error = None

        if not clientUrl:
            error = 'Webhook client url required'

        if error is not None:
            return (error, 400)
        
        else:
            # en caso de que no exista el registro, notificarlo
            db = get_db()
            db.execute(
                'DELETE FROM webhook_clients WHERE url = ?',
                (clientUrl,)
            )
            db.commit()

    return("Client registry deleted", 200)