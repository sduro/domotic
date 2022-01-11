'''
Pagina web para descargar mp3
config.json ->fichero de configuracion
'''
import json
import os
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
    print (option)
    bright = int(request.params.get('bright'))
    print (bright)
    url = "https://developer-api.govee.com/v1/devices/control"

    headers = CaseInsensitiveDict()
    headers["Govee-API-Key"] = datajson['configuration']['govee_api']
    headers["Content-Type"] = "application/json"
    mac=datajson['configuratio']['govee_bulb_mac']
    data = '{"device":"' +mac+'","model":"H6003","cmd":{"name":"turn","value":"' +option+'","name":"brightness","value":'+str(bright)+'}}'
    resp = requests.put(url, headers=headers, data=data)

    print(resp.status_code, resp.content)
    return template('static/control.html')

@route('/bright')
def bright():
    bright = request.params.get('bright')
    print (bright)
    url = "https://developer-api.govee.com/v1/devices/control"

    headers = CaseInsensitiveDict()
    headers["Govee-API-Key"] = datajson['configuration']['govee_api']
    headers["Content-Type"] = "application/json"
    mac=datajson['configuratio']['govee_bulb_mac']
    
    data = '{"device":"' +mac+'","model":"H6003","cmd":{"name":"turn","value":"on","name":"brightness","value":'+str(bright)+'}}'
    resp = requests.put(url, headers=headers, data=data)

    print(resp.status_code, resp.content)
    return template('static/control.html')

@route('/')
def menu():
    result = os.system('pip list | grep youtub'  ) 
    return template('static/main.html',path=result)

run(host='0.0.0.0', port=8088, debug=True)
