# GPX Time Offset
GPX Time Offset is a Python script that offsets the time of every record in a GPX file. It comes with a sleek UI that allows you to load a GPX file, offset the time as desired and save the modified file. Just run App.py on your computer.

[screenshot]: screenshots/main_ui.png
![screenshot]

## Background
"But, why?" you ask.

This project started off to address a personal need. I use a Mi Smart Band to record outdoor activites including running and cycling. It is a budget wearable device that gives you bang for the buck. For example, the latest model at the time of writing, Mi Band 9 Pro, has an official retail price of just MYR 269 (USD 60). It features an 1.74-inch AMOLED display, built-in GPS and up to 2 weeks' battery life.

Unfortunately, the app for the device, Mi Fitness can be erratic. One of the issues I often complain about is how it sometimes fails to sync an activity to Strava. Upon exporting the GPX to manually upload the activity, I found that the time is off by 8 hours! It appears that the app has a knack of neglecting the time zone when exporting data. Funnily, it happens intermittently without any trend.

This proves to be a frustration, but not enough for me to ditch the device. At least, not if I could do something about it. I decided I could write a script to rectify the GPX file. And so begins GPX Time Offset.

As of now, the app is not compiled into an executable file. I wouldn't want to run any unverified app downloaded off the internet, and you shouldn't, either. You could download the project and follow the steps below to setup and run. Or, you could always compile the project into an executable file yourself.

## How to Setup
1. [Install Python](https://www.python.org/downloads/)
2. Create a virtual environment:
```bash
python -m venv /path/to/new/virtual/environment
```
3. Navigate to the root directory of the project.
4. Activate virtual environment:
```bash
"./.venv/Scripts/Activate"
```
5. pip install the required packages:
```bash
pip install -r requirements.txt
```

## How to Run App
1. Navigate to the root directory of the project.
2. Activate virtual environment:
```bash
"./.venv/Scripts/Activate"
```
3. Run App.py:
```bash
python gpxtimeoffset/App.py
```