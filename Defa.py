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
GPIO.add_event_detect(IO_Bryter, GPIO.RISING)
mode = 0

####################################################

def Rele(Sta):
	GPIO.output(IO_Rele, Sta)
	print("Rele status: ", Sta)

def LED(mode):
	GPIO.output(IO_LED, Sta)
	print("LED status: ", Sta)
	
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


def Bryter():
	try:
		threading.Timer(0.3, Bryter).start()
			if GPIO.event_detected(IO_Bryter):
				mode = mode + 1
				if mode = 3
					mode = 0

		
	except KeyboadInterrupt:
		pass
		GPIO.cleanup()

#####################################################
######################  Main  #######################

if __name__ == '__main__':

	try:
		Bryter()
		#options[0]()
		Rele(0)

	except KeyboardInterrupt:
		pass	
		GPIO.cleanup()	
