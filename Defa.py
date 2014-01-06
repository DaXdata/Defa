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

#initialize 
import time
import RPi.GPIO as GPIO
import threading

IO_Bryter = 13
IO_LED = 11
IO_Rele = 7
GPIO.setmode(GPIO.BOARD)
GPIO.setup(IO_Rele, GPIO.OUT)
GPIO.setup(IO_LED, GPIO.OUT)
GPIO.setup(IO_Bryter, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
mode = 0
hFrom = 5
mFrom = 0
hTo = 7
mTo = 60

####################################################

def Rele(Sta):
	GPIO.output(IO_Rele, Sta)

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

def klokke_range(hFrom, hTo, mFrom, mTo):
		current = time.strftime("%H:%M")
		H = int(current[:2])
		M = int(current[3:])
		if hFrom <= H and H <= hTo and mFrom <= M and M <= mTo:
			return 1
		else:
			return 0
		time.sleep(6)
 
def auto():
	LED(0)
	Rele(klokke_range(hFrom, hTo, mFrom, mTo))

def off():
	LED(1)
	Rele(0)

def on():
	LED(1)
	Rele(1)

options = {0 : auto, 1 : off, 2 : on}


def Bryter(IO_Bryter):
	global mode
	mode = mode + 1
	if mode == 3:
		mode = 0
	print(mode)

GPIO.add_event_detect(IO_Bryter, GPIO.RISING, callback=Bryter, bouncetime=200)

#####################################################
######################  Main  #######################

if __name__ == '__main__':

	try:
		mode = 0
		flash_done = False
		while 1:	
			options[mode]()

	except KeyboardInterrupt:
		pass	
		GPIO.cleanup()	
