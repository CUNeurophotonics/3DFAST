# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 14:08:48 2022

@author: Researcher
"""

import serial 
import csv 
import pandas as pd 
import time 
import matplotlib.pyplot as plt
from operator import itemgetter


sensor_data = []

arduino = serial.Serial('COM8', timeout=.1)

fileName="Stims/Rec7.csv"
file = open(fileName, "a")

i = 0
while (i < 10000):
    #display the data to the terminal
    getData=arduino.readline()
    dataString = getData.decode('utf-8')
    data=dataString[0:][:-2]
    print(data)

    readings = data.split(" ")
    #print(readings)

    sensor_data.append(readings)
    #print(data)
    time.sleep(.0005)
    
    writer = csv.writer(file)
    writer.writerow(readings)
    
    
    
    
    i = i + 1

file.close()

second_column_vals = list(map(itemgetter(1), sensor_data))




i = 0
while i<10000:
    second_column_vals[i] = int(second_column_vals[i])
    i = i + 1

    

