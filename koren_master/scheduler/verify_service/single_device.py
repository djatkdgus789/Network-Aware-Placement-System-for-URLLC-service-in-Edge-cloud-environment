from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from requests import put, get, post
from ping3 import ping, verbose_ping

app = Flask(__name__)
api = Api(app)

@app.route('/api/rtt', methods=['GET'])
def rtt():
    node_ip = request.args.get('node_ip')
    print(type(node_ip))
    ip = str(node_ip)
    res = ping(ip)
    return { 'Image' : 'Galaxy', 'RTT' : res }



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

    
