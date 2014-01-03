#!/usr/bin/env python3

#initialize

import time
import RPi.GPIO as GPIO


Bryter = 13
LED = 11
Rele = 7
GPIO.setmode(GPIO.BOARD)
GPIO.setup(Rele, GPIO.OUT)
GPIO.setup(LED, GPIO.OUT)
GPIO.setup(Bryter, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
Toggle = False

#Toggle light

try:
	while True:
		if GPIO.input(Bryter) == True and Toggle == True:
			GPIO.output(LED, 1)
			Toggle = False
			print("Led On")			
			time.sleep(0.3)	

		if GPIO.input(Bryter) == True and Toggle == False:
			GPIO.output(LED, 0)
			Toggle = True
			print("Led Off")
			time.sleep(0.3)

except KeyboardInterrupt:
	pass	
GPIO.cleanup()	
