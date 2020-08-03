# Electricity Upload

Project for Raspberry Pi 3 to collect, store and upload electricity data from WiFi enable smart plug to AWS.

## Collecting Data
This project uses TP Link Energy Monitor project to analyse the signal from a TP Link smart plug on my home network.

See https://github.com/jamesbarnett91/tplink-energy-monitor

Can be installed using;

`git clone https://github.com/jamesbarnett91/tplink-energy-monitor
&& cd tplink -energy-monitor \
npm install \
npm start`

## Storing & Uploading Data
Data is then stored locally on the Raspberry Pi before being uploaded to AWS every night using `processing.py` sceduled with crontab.

In case any uploaded is missed (due to dropped network connection) a script has been included to upload data manually, `missed_upload.py`.
