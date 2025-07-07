#Importing from Files
from infer import predict
from sensor import read_acc
from infer import convert
from googlesheets import clear_values, update_values 

#Importing from libraries
import numpy as np
import torch
import time
import datetime
import json
import csv 
import RPi.GPIO as GPIO

##Button Pin Definition
button = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(button, GPIO.IN)

##Function to turn datetime into a JSON file
def serialize_datetime(obj):
	if isinstance(obj, datetime.datetime):
		return obj.isoformat()
		
## Data Labelling
data_labels = {0.0:"Walking", 1.0: "Walking Up", 2.0: "Walking Down", 3.0: "Sitting", 4.0: "Standing", 5.0: "Laying Down"}
data_overall = []

#Naming the Google Sheet
file_name = str(input('Enter a run name: '))
update_values('C1', 'RAW', [[file_name]])

##Clear Google sheets values
clear_values()
count = 0

##Collecting data
while GPIO.input(button) != False: 
	window = [[], [], []]
	window_size = 128	
		
	##Collecting 128 datapoints (2.56s) from sensor
	start = time.time()
	while len(window[0]) < window_size:
		ax, ay, az = read_acc()
		window[0].append(ax)
		window[1].append(ay)
		window[2].append(az)
		time.sleep(0.02)
	end = time.time()
	
	data_collection_time = f'{end - start:.2f}'
	
	data_overall.append(window)
	window = convert(window)
	prediction, con = predict(window)
	
	##Getting the date
	date = datetime.datetime.now()
	json_date = json.dumps(date, default=serialize_datetime)

	#Output to terminal
	print(f"Prediction: {data_labels[prediction]} \t Confidence: {round(con*100)}% \t Time: {date} \t Data Collect Time:{data_collection_time}")
	
	#Writing to Google Sheet 
	update_values(f'A{count+3}:D{count+3}', 'RAW', [[json_date, data_labels[prediction], float(con), data_collection_time]])
	count += 1

