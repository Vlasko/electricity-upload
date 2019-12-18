# Standard Library Imports
import os


# Third Party Imports
import requests
from datetime import datetime

# Local Application Imports
from keys.octopus_keys import API_Key

def price_store():
    today = datetime.now().date().strftime('%Y-%m-%d')
    directory = os.getcwd()
    try:
        today = datetime.now().date().strftime('%Y-%m-%d')
        with open(directory+'/files/prices/'+today+'_prices.csv', 'w+') as g:
            if os.stat(directory+'/files/prices/'+today+'_prices.csv').st_size == 0: #This checks if file is empty
                g = open(directory+'/files/prices/'+today+'_prices.csv', 'w+')
                g.write('Timestamp,Electricity Price(p/kWh)\r\n')

    except:
        print('f error')
        pass

    address = 'https://api.octopus.energy/v1/products/AGILE-18-02-21/electricity-tariffs/E-1R-AGILE-18-02-21-C/standard-unit-rates/'
    response = requests.get(address,
                          auth=(API_Key, ''))
    json = response.json()
    data = json['results']

    with open(directory+'/files/prices/'+today+'_prices.csv', 'a+') as g:
        if data is not None:
            for entry in data[0:48][::-1]:
                line = '{0},{1}\n'.format(datetime.strptime(entry['valid_from'], '%Y-%m-%dT%H:%M:%SZ').strftime('%Y-%m-%d %H:%M:%S'),
                                             entry['value_inc_vat'])
                g.write(line)
            g.close()
        else:
            print("Failed to retrieve price data from Octopus API")
