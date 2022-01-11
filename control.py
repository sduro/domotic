import requests
from requests.structures import CaseInsensitiveDict

def turnon():
    url = "https://developer-api.govee.com/v1/devices/control"

    headers = CaseInsensitiveDict()
    headers["Govee-API-Key"] = "c64dcd4a-0a5b-4153-8798-177e606f34e2"
    #headers["Request Method"] = "PUT"
    headers["Content-Type"] = "application/json"

    data = '{"device":"df:db:7c:a6:b0:11:47:ab","model":"H6003","cmd":{"name":"brightness","value":100}}'
    resp = requests.put(url, headers=headers, data=data)

    data = '{"device":"df:db:7c:a6:b0:11:47:ab","model":"H6003","cmd":{"name":"turn","value":"off"}}'
    resp = requests.put(url, headers=headers, data=data)

    print(resp.status_code, resp.content)

    return True

def bright():
    url = "https://developer-api.govee.com/v1/devices/control"

    headers = CaseInsensitiveDict()
    headers["Govee-API-Key"] = "c64dcd4a-0a5b-4153-8798-177e606f34e2"
    #headers["Request Method"] = "PUT"
    headers["Content-Type"] = "application/json"

    data = '{"device":"df:db:7c:a6:b0:11:47:ab","model":"H6003","cmd":{"name":"brightness","value":100}}'
    resp = requests.put(url, headers=headers, data=data)

    data = '{"device":"df:db:7c:a6:b0:11:47:ab","model":"H6003","cmd":{"name":"turn","value":"off"}}'
    resp = requests.put(url, headers=headers, data=data)

    print(resp.status_code, resp.content)

    return True