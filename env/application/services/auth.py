import http.client
import json


def authentication():
    conn = http.client.HTTPSConnection("desenvolvimento.arkmeds.com")
    payload = {"email": "testedev@arkmeds.com", "password": "testedev"}
    headers = {'Content-Type': 'application/json'}
    conn.request("POST", "/rest-auth/token-auth/",
                 json.dumps(payload), headers)
    res = conn.getresponse()
    data = res.read()
    return json.loads(data)


def make_connection():
    token = authentication()["token"]  # Isso pega o token
    conn = http.client.HTTPSConnection("desenvolvimento.arkmeds.com")
    headers = {
        'Authorization': 'JWT {}'.format(token),
        'Content-Type': 'application/json'
    }
    return conn, headers
