import os
import time
import Adafruit_DHT
import requests
from datetime import datetime

path_prefix = os.path.split(os.getcwd())[0]

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4


def temperature_pull():
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)

    return temperature, humidity

def temperature_store():
    today = datetime.now().date().strftime('%Y-%m-%d')
    try:
        f = open(path_prefix+'/Fridge_Flex/Files/Temperature/'+today+'_temperature.csv', 'a+')
        if os.stat(path_prefix+'/Fridge_Flex/Files/Temperature/'+today+'_temperature.csv').st_size == 0:
                f.write('Timestamp,Temperature (*C),Humidity (%)\r\n')
    except:
        print('open error')
        pass

    temperature, humidity = temperature_pull()

    if humidity is not None and temperature is not None:
        f.write('{0},{1:0.2f},{2:0.1f}\r\n'.format(time.strftime('%Y-%m-%dT%H:%M:00Z'), temperature, humidity))
    else:
        print("Failed to retrieve data from humidity sensor")
        requests.post('https://maker.ifttt.com/trigger/temperature_failure/with/key/dbcGxPSBCligASFX4fRk3p')

    return temperature, humidity
