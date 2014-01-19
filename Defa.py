#!/usr/bin/env python3 

#################################################
# This script is written to run a Defa warmup   #
# reley mounted outside. it should start the	#
# fan and motor heater at a given time. mode	#
# can be selected from a switch or UDP data.	#
#################################################
#						#
# V0.0 , JAET , First version			#
# V1.0 , JAET , Switch and clock mode		#
# V1.1 , JAET , Runs as Service			#
#						#
#################################################
#Runs as service at startup,			#
#Start:  sudo /etc/init.d/defa.sh start		#
#Status:  sudo /etc/init.d/defa.sh status	#
#Stop:  sudo /etc/init.d/defa.sh stop		#
#################################################

#################################################
#                 initialize                    # 
#################################################

### Imports
import time
import RPi.GPIO as GPIO
import threading
from UDP import UDP
from Parse import Parse

### Input/Output
IO_Bryter = 13
IO_LED = 11
IO_Rele = 7
GPIO.setmode(GPIO.BOARD)
GPIO.setup(IO_Rele, GPIO.OUT)
GPIO.setup(IO_LED, GPIO.OUT)
GPIO.setup(IO_Bryter, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

### Communication
com = UDP(30301,30302)
p = Parse

### Variables
mode = 0
hOn = 5
mOn = 0
hOff = 7
mOff = 60

#################################################
#                 Functiuons                    # 
#################################################

### Rele Output
def Rele(Sta):
	GPIO.output(IO_Rele, Sta)

### Led Output
def LED(mode):
	global flash_done
	if mode == 0 and not flash_done:
		for n in range(0,10):
			#(n % 2) gir 1 ved oddetall, og 0 ved partall
			GPIO.output(IO_LED, (n % 2))
			#print("LED status: auto")
			time.sleep(0.2)
		flash_done = True
	if mode == 0 and flash_done:
		GPIO.output(IO_LED, GPIO.input(IO_Rele))

	if mode == 1:
		GPIO.output(IO_LED, GPIO.input(IO_Rele))
		flash_done = False

### Clock / Timing function
def klokke_range(hOn, hOff, mOn, mOff):
		current = time.strftime("%H:%M")
		H = int(current[:2])
		M = int(current[3:])
		if hOn <= H and H <= hOff and mOn <= M and M <= mOff:
			return 1
		else:
			return 0
		time.sleep(6)

### Modes
def auto():
	LED(0)
	Rele(klokke_range(hOn, hOff, mOn, mOff))

def off():
	LED(1)
	Rele(0)

def on():
	LED(1)
	Rele(1)

options = {2 : auto, 0 : off, 1 : on}

### Parsing from UDP
def get_cmd(data):
	global mode, hOn, mOn, hOff, mOff
#Time On
	ret_tOn = p.getTimeOn(com.data)
	print(ret_tOn)
	if ret_tOn[0] is True:
		hOn = int(ret_tOn[1])
		mOn = int(ret_tOn[2])
		text = "Time On: " + ret_tOn[1] + ":" + ret_tOn[2]
		com.send_udp(text)
#Time Off
	ret_tOff = p.getTimeOff(com.data)
	print(ret_tOff)
	if ret_tOff[0] is True:
		hOff = int(ret_tOff[1])
		mOff = int(ret_tOff[2])
#Mode selected
	ret_mode = p.getMode(com.data)
	if ret_mode[0] is True:
		mode = int(ret_mode[1])	
		print("Mode: =", mode)

### Increment to next mode
def Bryter(IO_Bryter):
	global mode
	mode = mode + 1
	if mode == 3:
		mode = 0

	if mode == 2:
		print("Mode: Auto")
	if mode == 0:
		print("Mode: Off")
	if mode == 1:
		print("Mode: On")
#	options[mode]()

### Watching Input
GPIO.add_event_detect(IO_Bryter, GPIO.RISING, callback=Bryter, bouncetime=200)

#################################################
#                 Main Loop                     # 
#################################################

### Declaration
if __name__ == '__main__':

	try:
		mode = 2
		flash_done = False
		print("Defa Running")
		com.data = None
		while 1:	
			options[mode]()
			com.recv_udp()
			if com.data is not None:
				get_cmd(com.data)
				com.data = None
			time.sleep(0.1)
	except KeyboardInterrupt:
		pass	
		GPIO.cleanup()	
		com.stop()
