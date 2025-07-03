from infer import predict
from sensor import read_acc
from infer import convert
import numpy as np
import torch
import time
import RPi.GPIO as GPIO

#Data Labels
data_labels = {0.0:"Walking", 1.0: "Walking Up", 2.0: "Walking Down", 3.0: "Sitting", 4.0: "Standing", 5.0: "Laying Down"}

##Button Pin Definition
button = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(button, GPIO.IN)

#Setting up data collection
data_overall = []

while GPIO.input(button) != False: 
	window = [[], [], []]
	window_size = 128	

	while len(window[0]) < window_size:
		ax, ay, az = read_acc()
		window[0].append(ax)
		window[1].append(ay)
		window[2].append(az)
		time.sleep(0.02)
	
	data_overall.append(window)
	window = convert(window)
	prediction, con = predict(window)
	
	
	print(f"Prediction: {data_labels[prediction]} \t Confidence: {round(con*100)}%")
	
