# Standard Library Imports
import os
from time import sleep
import requests

#Third Party Imports
from datetime import datetime
# from subprocess import call

# Local Application Imports
from functions.demand_functions import current_demand_json_to_csv
from functions.aws_functions import upload_to_aws
from functions.price_functions import price_store

bucket_name= ['elecprices', 'elecdemand']

def upload_demand():
    directory = os.getcwd()
    price_store()
    print('price stored')
    today =  datetime.now().date().strftime('%Y-%m-%d')

    # Prices
    upload_to_aws(directory+'/files/prices/'+ today +'_prices.csv',
                  bucket_name[0], today +'_prices.csv')
    # Demand
    current_demand_json_to_csv()
    upload_to_aws(directory+'/files/demand/'+ today +'_demand.csv',
                  bucket_name[1], today +'_demand.csv')

try:
    upload_demand()
    requests.post('https://maker.ifttt.com/trigger/upload_event/with/key/dbcGxPSBCligASFX4fRk3p')
except Exception as e:
    print(e)
    requests.post('https://maker.ifttt.com/trigger/upload_error/with/key/dbcGxPSBCligASFX4fRk3p')

print(datetime.now())
