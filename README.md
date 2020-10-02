# Electricity Upload

Project for Raspberry Pi 3 to collect, store and upload electricity demand and price data from WiFi enable smart plug to AWS S3. It works in conjunction with https://github.com/Vlasko/electricity-processing which allows for processing of the data.

To use this project AWS and Octopus API keys will need to be saved in the necessary folders.

Code is run on Raspberry Pi using SSH and the terminal multiplexer, Screen.

## Set Up
### Set Up Octopus API & AWS Buckets
Create an account for AWS taking note of your `ACCESS_KEY` and `SECRET_KEY`. Create two S3 buckets named `elecprices` and `elecdemand`. Create an account for the Octopus Energy API, taking note of your `API_Key`. Create two files with the following format;

keys/AWS_keys.py
```
    ACCESS_KEY = 'insert_key'
    SECRET_KEY = 'insert_key'
```

keys/octopus_keys.py
```
    API_Key = 'insert_key'
```
### Set Up Energy Monitor
The project uses TP Link Energy Monitor project to analyse the signal from a TP Link smart plug on my home network. See https://github.com/jamesbarnett91/tplink-energy-monitor for more details.

Clone this repo onto your Raspberry Pi by running

```
git clone https://github.com/Vlasko/electricity-upload && cd electricity-upload
```

Then install TP Link Energy Monitor

```   
    git clone https://github.com/jamesbarnett91/tplink-energy-monitor
    cd tplink-energy-monitor
    npm install
```

A new screen session should be started to ensure that the SSH session used for data collection does not drop. Naming the session helps with identifying later on.

```
    screen -S data_collection
    npm start
```
### Schedule Download/Upload
Crontab should be used to schedule `processing.py` once every day. This script will;
- download electricity price data from the Octopus API
- upload electricity price data to AWS S3 bucket
- convert electricity demand data from json format to csv format
- upload electricity demand data to AWS S3 bucket

To schedule running of script run `crontab -e` and add the following line;
```
    59 23 * * * cd Documents/Projects/electricity-upload && python processing.py >> cron.log 2>&1
```

In case any uploaded is missed (due to dropped network connection) a script has been included to upload data manually, `missed_upload.py`. `cron.log` is used to keep track of each time the data is uploaded to AWS.

# To Do
- [x] Update ReadMe
- [X] Amend keys storage to allow other users to save their own keys
- [ ] Create `setup.py` to create necessary file structure to store data, and amend the json logger from tplink-energy-monitor
- [ ] Enable automated running of `npm` file that runs on startup or if an error is encountered
