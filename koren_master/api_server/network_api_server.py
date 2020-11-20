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
    node_dict = {'seoul':'http://116.89.189.24:3000/api/rtt/',
                'daejeon':'http://103.22.222.240:3000/api/rtt/',
                'idpl':'http://117.17.158.68:3000/api/rtt/'}

    print("get from edge node")
    daejeon = get('http://103.22.222.240:3000/api/rtt/',params=params)
    seoul = get('http://116.89.189.24:3000/api/rtt/',params=params)
    # idpl = get('http://117.17.158.60:5707/api/rtt/',params=params)
    print(daejeon.json())
    print(seoul.json())
    # print(idpl.json())
    network_status = dict()
    network_status["idpl-dj"] = daejeon.json()
    network_status["suwon"] = seoul.json()
    # print(network_status)
    return json.dumps(network_status)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)
