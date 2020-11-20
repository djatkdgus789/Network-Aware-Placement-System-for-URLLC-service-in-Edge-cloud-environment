from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from requests import put, get, post


import sys, time
from socket import socket,AF_INET, SOCK_STREAM
import threading
import unicodedata


app = Flask(__name__)
api = Api(app)

@app.route('/api/rtt/', methods=['GET'])
def rtt():
    node_ip = request.args.get('node_ip')
    print(type(node_ip))
    ip = str(node_ip)
    count = 100
    port =9999
    BUFSIZE = 1024000
    testdata = 'x' * (BUFSIZE-1) + '\n'
    t1 = time.time()
    s = socket(AF_INET, SOCK_STREAM)
    t2 = time.time()
    s.connect((ip, int(port)))
    t3 = time.time()
    i = 0
    while i < count:
        i = i+1
        s.send(bytearray(testdata,"utf-8"))
    s.shutdown(1)
    t4 = time.time()
    data = s.recv(BUFSIZE)
    t5 = time.time()
    print (data.decode())
    print ('ping:', (t3-t2)+(t5-t4)/2)
    print ('Time:', t4-t3)
    print ('Bandwidth:', round((BUFSIZE*count*0.001) / (t4-t3), 3),)
    print ('Kb/sec.')
    return {'ip' : node_ip,
            'ping': (t3-t2)+(t5-t4)/2,
            'time': t4-t3,
            'bandwidth': float(round((BUFSIZE*count*0.001) / (t4-t3), 3),)}



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)

    
