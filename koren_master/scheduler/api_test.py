import requests
import json
network_status = requests.get('http://10.20.12.83:4000/api/rtt/'+"10.20.12.83")
# logger.info(network_status.json())
    # filtering by rtt
#print(network_status.json())
#print(type(network_status.json))
# json = json.loads(network_status.json())
rtt = dict()
bdw = dict()

for network in network_status.json():
    #print(network)
    rtt[network[1].get('ping')] =  network[0]
    bdw[network[1].get('bandwidth')] = network[0]
    


print(rtt)
print(bdw)
    
minRttNode = rtt.get(min(rtt.keys()))
print('Scheduler select feasible node : ' + str(minRttNode))

