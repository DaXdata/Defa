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

####################################################

def Rele(Sta):
	GPIO.output(IO_Rele, Sta)
	GPIO.output(IO_LED, Sta)
	print("Rele status: ", Sta)

def klokke_range(start=5, stopp=8):
	threading.Timer(10, klokke_range).start()

time.fsrtime("%H:%M")
#plukk ut verdi for tid av string
sammenlign med en grense gitt av funksjonen.

def Bryter():
Toggle = True
	threading.Timer(0.3, Bryter).start()
		if GPIO.input(IO_Bryter) == True and Toggle == True:
			Rele(1)
			Toggle = False


		if GPIO.input(IO_Bryter) == True and Toggle == False:
			Rele(0)
			Toggle = True


#####################################################
######################  Main  #######################

if __name__ == '__main__':

	try:
		klokke_range(3,4)
		Bryter()

	except KeyboardInterrupt:
		pass	
		GPIO.cleanup()	
