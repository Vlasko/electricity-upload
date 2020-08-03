# Electricity Upload

Project for Raspberry Pi 3 to collect, store and upload electricity demand and price data from WiFi enable smart plug to AWS S3. It works in conjunction with https://github.com/Vlasko/electricity-processing which allows for processing of the data.

To use this project AWS and Octopus API keys will need to be saved in the necessary folders.

Code is run on Raspberry Pi using SSH and linux screen tool.

## Collecting Data
This project uses TP Link Energy Monitor project to analyse the signal from a TP Link smart plug on my home network.

See https://github.com/jamesbarnett91/tplink-energy-monitor

Once in the `electricity-upload` directory it should be installed using;

`    git clone https://github.com/jamesbarnett91/tplink-energy-monitor
    cd tplink -energy-monitor
    npm install
    npm start`

Electricity price data is also downloaded from the Octopus API.

## Storing & Uploading Data
Data is then stored locally on the Raspberry Pi before being uploaded to AWS every night using `processing.py` sceduled with crontab.

In case any uploaded is missed (due to dropped network connection) a script has been included to upload data manually, `missed_upload.py`.

`cron.log` is used to keep track of each time the data is uploaded to AWS.

# To Do
- [x] Update ReadMe
- [ ] Amend keys storage to allow other users to save their own keys
- [ ] Create `setup.py` to create necessary file structure to store data, and amend the json logger from tplink-energy-monitor
- [ ] Enable automated running of `npm` file that runs on startup or if an error is encountered
