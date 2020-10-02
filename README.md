# Electricity Upload

Project for Raspberry Pi 3 to collect, store and upload electricity demand and price data from WiFi enable smart plug to AWS S3. It works in conjunction with https://github.com/Vlasko/electricity-processing which allows for processing of the data.

To use this project AWS and Octopus API keys will need to be saved in the necessary folders.

Code is run on Raspberry Pi using SSH and the terminal multiplexer, Screen.

## Set Up
### Collecting Data
This project uses TP Link Energy Monitor project to analyse the signal from a TP Link smart plug on my home network.

See https://github.com/jamesbarnett91/tplink-energy-monitor

Get into the right directory by running, `cd electricity-upload` and then install the above project using;

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

Crontab should be used to schedule `processing.py` once every day. This script will;
- scrape electricity price data from the Octopus API
- upload electricity price data to AWS S3 bucket
- convert electricity demand data from json format to csv format
- upload electricity demand data to AWS S3 bucket

To schedule running of script run `crontab -e` and add the following line;
```
    59 23 * * * cd Documents/Projects/electricity-upload && python processing.py
```

## Storing & Uploading Data
Data is then stored locally on the Raspberry Pi before being uploaded to AWS every night using `processing.py` sceduled with crontab.

In case any uploaded is missed (due to dropped network connection) a script has been included to upload data manually, `missed_upload.py`.

`cron.log` is used to keep track of each time the data is uploaded to AWS.

# To Do
- [x] Update ReadMe
- [ ] Amend keys storage to allow other users to save their own keys
- [ ] Create `setup.py` to create necessary file structure to store data, and amend the json logger from tplink-energy-monitor
- [ ] Enable automated running of `npm` file that runs on startup or if an error is encountered
