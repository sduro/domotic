'''
Pagina web para descargar mp3
config.json ->fichero de configuracion

Demos:
    {"name": "turn", value: "oﬀ"}
    {"name": "brightness", value: 10}
    {"name": "color", value: {"r": 255, "g": 255, "b": 255}}
    {"name": "colorTem", value: 7000}
'''
import json
import os
from urllib import response
from matplotlib.pyplot import switch_backend
import requests
from requests.structures import CaseInsensitiveDict
from bottle import run, get, post, request, template, route,static_file,redirect, view # or route

with open("config.json", "r") as jsonfile:
    datajson = json.load(jsonfile) # Reading the file
    jsonfile.close()

def config():
    with open("config.json", "w") as jsonfile:
        json.dump(datajson,jsonfile,ensure_ascii=False) # writing the file
        jsonfile.close()

@route("/static/css/<filename>")
def server_static(filename):
	return static_file(filename,root="./static/css")

@route('/govee')
def control():
    return template('static/control.html')

@route('/control')
def control():
    option = request.params.get('option')
    url = "https://developer-api.govee.com/v1/devices/control"
    headers = CaseInsensitiveDict()
    headers["Govee-API-Key"] = datajson['configuration']['govee_api']
    headers["Content-Type"] = "application/json"
    mac=datajson['configuration']['govee_bulb_mac']

    if option=='status':
            bright = int(request.params.get('bright'))
            data = '{"device":"' +mac+'","model":"H6003","cmd":{"name":"turn","value":"' +option+'","name":"brightness","value":'+str(bright)+'}}'
            resp = requests.put(url, headers=headers, data=data)
    elif option=='color':
            r = int(request.params.get('r'))
            g = int(request.params.get('g'))
            b = int(request.params.get('b'))
            #{"name": "color", value: {"r": 255, "g": 255, "b": 255}}
            data = '{"device":"' +mac+'","model":"H6003","cmd":{"name":"turn","value":"' +option+'","name":"color","value":{"r":'+str(r)+',"g":'+str(g)+',"b":'+str(b)+'}}}'
            resp = requests.put(url, headers=headers, data=data)
    print(resp.status_code, resp.content)
    return template('static/control.html')

@route('/bright', method='GET')
def bright():
    response.content_type='application/json'
    receiver = request.json['bright']
    bright = request.params.get('bright')
    print(receiver)

    url = "https://developer-api.govee.com/v1/devices/control"

    headers = CaseInsensitiveDict()
    headers["Govee-API-Key"] = datajson['configuration']['govee_api']
    headers["Content-Type"] = "application/json"
    mac=datajson['configuration']['govee_bulb_mac']
    
    data = '{"device":"' +mac+'","model":"H6003","cmd":{"name":"turn","value":"on","name":"brightness","value":'+str(bright)+'}}'
    resp = requests.put(url, headers=headers, data=data)

    print(resp.status_code, resp.content)
    return template('static/control.html')

@route('/')
def menu():
    return template('static/control.html')

run(host='0.0.0.0', port=8088, debug=True)
