# Standard Library Imports
import os
from time import sleep

#Third Party Imports
from datetime import datetime
# from subprocess import call

# Local Application Imports
from functions.demand_functions import current_demand_json_to_csv
from functions.aws_functions import upload_to_aws
from functions.price_functions import price_store

#call(['node', './tplink-energy-monitor/app.js'])

def upload_demand():
    directory = os.getcwd()
    price_store()
    print('price stored')
    today =  datetime.now().date().strftime('%Y-%m-%d')

    # Prices
    upload_to_aws(directory+'/files/prices/'+ today +'_prices.csv',
                  'lukaprices', today +'_prices.csv')
    # Demand
    current_demand_json_to_csv(directory+'/files/demand/8006AD6134CA39AE8FD966D4E1A709821B20C760-log.json')
    upload_to_aws(directory+'/files/demand/'+ today +'_demand.csv',
                  'fridgedemand', today +'_demand.csv')

# condition = False
# while condition == False:
#     if datetime.now().hour == 23 and datetime.now().minute == 59:
#         upload_demand()
#         sleep(60)
