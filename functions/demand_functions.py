# Standard Library Imports
import os

# Third Party Imports
import json
from datetime import datetime

def generic_demand_json_to_csv(json_path, name):
    directory = os.getcwd()
    f = open(directory+'/files/demand/'+name+'_demand.csv', 'a+')
    if os.stat(directory+'/files/demand/'+name+'_demand.csv').st_size == 0:
            f.write('Timestamp,Demand (W)\r\n')

    demand_file = directory + json_path

    with open(demand_file) as g:
        demand_list = json.load(g)
        for entry in demand_list:
            javascript_time = entry['ts']
            timestamp = datetime.fromtimestamp(javascript_time/1000)
            # aware_timestamp = pytz.utc.localize(timestamp)
            power = entry['pw']

            if power is not None :
                f.write('{0},{1:0.2f}\r\n'.format(timestamp.strftime('%Y-%m-%dT%H:%M:00Z'), power))

def current_demand_json_to_csv():
    directory = os.getcwd()
    today = str(datetime.now().date())

    f = open(directory+'/files/demand/'+today+'_demand.csv', 'a+')
    if os.stat(directory+'/files/demand/'+today+'_demand.csv').st_size == 0:
            f.write('Timestamp,Demand (W)\r\n')

    demand_file = directory + '/tplink-energy-monitor/8006AD6134CA39AE8FD966D4E1A709821B20C760-log.json'

    with open(demand_file) as g:
        demand_list = json.load(g)
        for entry in demand_list:
            javascript_time = entry['ts']
            timestamp = datetime.fromtimestamp(javascript_time/1000)
            # aware_timestamp = pytz.utc.localize(timestamp)
            power = entry['pw']

            if power is not None :
                f.write('{0},{1:0.2f}\r\n'.format(timestamp.strftime('%Y-%m-%dT%H:%M:00Z'), power))

def demand_json_to_csv(json_path):
    directory = os.getcwd()
    date = json_path[13:23]

    f = open(directory+'/files/demand/'+date+'_demand.csv', 'a+')
    if os.stat(directory+'/files/demand/'+date+'_demand.csv').st_size == 0:
            f.write('Timestamp,Demand (W)\r\n')

    demand_file = directory + json_path

    with open(demand_file) as g:
        demand_list = json.load(g)
        for entry in demand_list:
            javascript_time = entry['ts']
            timestamp = datetime.fromtimestamp(javascript_time/1000)
            # aware_timestamp = pytz.utc.localize(timestamp)
            power = entry['pw']

            if power is not None :
                f.write('{0},{1:0.2f}\r\n'.format(timestamp.strftime('%Y-%m-%dT%H:%M:00Z'), power))
