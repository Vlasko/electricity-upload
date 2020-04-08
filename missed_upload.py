# Standard Library Imports
import os

# Third Party Imports


# Local Application Imports
from functions.demand_functions import generic_demand_json_to_csv

directory = os.getcwd()
json_path = '/tplink-energy-monitor/8006AD6134CA39AE8FD966D4E1A709821B20C760-log.json'

generic_demand_json_to_csv(json_path, '2020-04-07')
