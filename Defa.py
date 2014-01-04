#!/usr/bin/env python3 

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

####################################################

def Rele(Sta):
	GPIO.output(IO_Rele, Sta)
	print("Rele status: ", Sta)

def LED(mode):
	if mode == 0:
		GPIO.output(IO_LED, 1)
		print("LED status: auto")
	if mode == 1:
		GPIO.output(IO_LED, 0)
		print("LED status: off")
	if mode == 2:		
		GPIO.output(IO_LED, 1)
		print("LED status: on")

def klokke_range(start=5, stopp=8):
	threading.Timer(10, klokke_range).start()
		#current = time.strftime("%H:%M")
		#print(current)

def auto():
	LED(auto)
	#klokke_range(fra, til)

def off():
	LED(off)
	threading.Timer(10, klokke_range).stop()
	
def on():
	LED(on)
	threading.Timer(10, klokke_range).stop()

options = {0 : auto, 1 : off, 2 : on}


def Bryter(IO_Bryter):
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
		while 1:	
			options[mode]()

	except KeyboardInterrupt:
		pass	
		GPIO.cleanup()	
