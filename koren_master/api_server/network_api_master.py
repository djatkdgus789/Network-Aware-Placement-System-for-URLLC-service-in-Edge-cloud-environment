from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from requests import put, get, post
import json

app = Flask(__name__)
api = Api(app)

@app.route('/api/rtt/<node_ip>') 
def rtt(node_ip):
    params = {'node_ip':node_ip}
    # network_status = json()

    print("get from edge node")
    whale01 = get('http://10.20.12.83:3000/api/rtt/',params=params)
    whale02 = get('http://10.20.12.84:3000/api/rtt/',params=params)
    whale03 = get('http://10.20.12.85:3000/api/rtt/',params=params)
    whale04 = get('http://10.20.12.86:3000/api/rtt/',params=params)
    whale06 = get('http://10.20.12.88:3000/api/rtt/',params=params)
    whale07 = get('http://10.20.12.89:3000/api/rtt/',params=params)
    whale08 = get('http://10.20.12.90:3000/api/rtt/',params=params)
    whale09 = get('http://10.20.12.91:3000/api/rtt/',params=params)
    whale10 = get('http://10.20.12.92:3000/api/rtt/',params=params)

    #print(whale01.json())
    #print(whale02.json())
    #print(whale03.json())
    #print(whale04.json())
    #print(whale06.json())
    #print(whale07.json())
    #print(whale08.json())
    #print(whale09.json())
    #print(whale10.json())

    network_status = dict()
    network_status["whale01"] = whale01.json()
    network_status["whale02"] = whale02.json()
    network_status["whale03"] = whale03.json()
    network_status["whale04"] = whale04.json()
    network_status["whale06"] = whale06.json()
    network_status["whale07"] = whale07.json()
    network_status["whale08"] = whale08.json()
    network_status["whale09"] = whale09.json()
    network_status["whale10"] = whale10.json()
    network_status = sorted(network_status.items())
    #for k, v in network_status.items():
    #    print(k)
    #    for v1, v2 in v.items():
    #        print(v1, v2)
    #print(network_status)
    return json.dumps(network_status)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)
