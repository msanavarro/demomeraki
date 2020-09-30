#!flask/bin/python

"""
Cisco Meraki Location Scanning Receiver

The provided sample code in this repository will reference this file to get the
information needed to connect to your lab backend.  You provide this info here
once and the scripts in this repository will access it as needed by the lab.
Copyright (c) 2019 Cisco and/or its affiliates.
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

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

############## USER DEFINED SETTINGS ###############
# MERAKI SETTINGS
validator = "306a9222c09aa429406472217e7333224d3628ad"
secret = "SantoYSena"
version = "2.0" 
locationdata = "Location Data Holder"
# WEBEX API SETTINGS
url = "https://api.ciscospark.com/v1/messages"
headers = {
  'Authorization': 'Bearer MDIwMmFmNmEtMjczMi00MTc2LTg0YzgtMThjMzgxMjBiMTllZjhhODJmOTktODUw_PF84_consumer',
  'Content-Type': 'application/json'
}
####################################################
bp = Blueprint('locationscanning', __name__)


# Respond to Meraki with validator

active_alarms = list()


@bp.route("/", methods=["GET"])
def get_validator():
    print("validator sent to: ", request.environ["REMOTE_ADDR"])
    return validator


# Accept CMX JSON POST


@bp.route("/", methods=["POST"])
def get_locationJSON():
    global locationdata

    if not request.json or not "data" in request.json:
        return ("invalid data", 400)

    locationdata = request.json
    '''
    locationdata ES EL PAQUETE DE INFORMACION DONDE ESTAN LOS APs, SUS CLIENTES Y UBICACIONES
    ES UN DICCIONARIO, POR LO QUE ACCEDER A LA INFORMACION ES ALGO TRIVIAL 
    '''
    print("Received POST from ", request.environ["REMOTE_ADDR"])

    # Verify secret
    if locationdata["secret"] != secret:
        print("secret invalid:", locationdata["secret"])
        return ("invalid secret", 403)

    else:
        print("secret verified: ", locationdata["secret"])

    # Verify version
    if locationdata["version"] != version:
        print("invalid version")
        return ("invalid version", 400)

    else:
        print("version verified: ", locationdata["version"])

    # Determine device type
    if locationdata["type"] == "DevicesSeen":
        db = get_db()
        i = 1
        for value in locationdata["data"]["observations"] :
            macaddr = (value["clientMac"],)
            exists = db.execute("SELECT EXISTS(SELECT 1 FROM visits WHERE macaddr=?)", macaddr);
            if(exists.fetchone()[0]==0):
                db.execute(
                    'INSERT INTO visits (macaddr)'
                    ' VALUES (?)',
                    (value["clientMac"],)
                )
            if any(d['macaddr'] == value["clientMac"] for d in active_alarms):
                print("Alarma antes: {}".format(active_alarms))
                payload = "{\n  \"roomId\": \"Y2lzY29zcGFyazovL3VzL1JPT00vOTUxNjhjODAtYjRkOC0xMWVhLWE4NjgtM2I1NDc5YzA0NzQz\",\n  \"text\": \"Se conecto Hugo\"\n}"
                response = requests.request("POST", url, headers=headers, data = payload)
                res = list(filter(lambda i: i['macaddr'] != value["clientMac"], active_alarms))
                print("Alarma despues: {}".format(res))
                print(response.text.encode('utf8'))
            i += 1
        db.commit()
        
            
        print("WiFi Devices Seen")
    elif locationdata["type"] == "BluetoothDevicesSeen":
        print("Bluetooth Devices Seen")
    else:
        print("Unknown Device 'type'")
        return ("invalid device type", 403)

    # Return success message
    return "Location Scanning POST Received"


@bp.route("/go", methods=["GET"])
def get_go():
    return render_template("index.html", **locals())

@bp.route("/widget", methods=["GET"])
def get_widget():
    return render_template("widget.html", **locals())


@bp.route("/clients/", methods=["GET"])
def get_clients():
    global locationdata
    if locationdata != "Location Data Holder":
        # pprint(locationdata["data"]["observations"], indent=1)
        return json.dumps(locationdata["data"]["observations"])

    return ""


@bp.route("/clients/<clientMac>", methods=["GET"])
def get_individualclients(clientMac):
    global locationdata
    for client in locationdata["data"]["observations"]:
        if client["clientMac"] == clientMac:
            return json.dumps(client)

    return ""

@bp.route("/alarms", methods=["POST"])
def set_alarm():
    if not request.json or not "data" in request.json:
        return ("invalid data", 400)

    people = request.json
    
    print("Received POST from ", request.environ["REMOTE_ADDR"])
    i = 1
    for value in people["data"]:
        print(i, value["name"], value["macaddr"])
        active_alarms.append(value)
        print(active_alarms)
        i += 1
    # Return success message
    return "Location Scanning POST Received"

# Launch application with supplied arguments


def main(argv):
    global validator
    global secret

    try:
        opts, args = getopt.getopt(argv, "hv:s:", ["validator=", "secret="])
    except getopt.GetoptError:
        print("locationscanningreceiver.py -v <validator> -s <secret>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-h":
            print("locationscanningreceiver.py -v <validator> -s <secret>")
            sys.exit()
        elif opt in ("-v", "--validator"):
            validator = arg
        elif opt in ("-s", "--secret"):
            secret = arg

    print("validator: " + validator)
    print("secret: " + secret)


if __name__ == "__main__":
    main(sys.argv[1:])
    app.run(ssl_context='adhoc', host="0.0.0.0", port=5002, debug=False)
