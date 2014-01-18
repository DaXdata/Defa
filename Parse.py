#!/usr/bin/env python3

#################################################
# This script will take a UDP string and        #
# return variable values used by Defa Warmup.   #
#################################################
#                                               #
# V0.0 , JAET , First version                   #
#						#
#################################################

#################################################
#                  initialize                   #
#################################################

### Imports	


### Declaire
tOn = "-On"
tOff = "-Off"
mode = "-M"

#################################################
#		    Create class		#
#################################################

class Parse:


	def getTimeOn(data):
		data = data.decode()
		try:
			command = data.split(" ")
			if tOn in command:
				temp = command[command.index(tOn) + 1]
				temp = temp.split(":")
				hOn = temp[0]
				mOn = temp[1]
				print("mottat tid On: ", hOn, ":", mOn)
				return(True, hOn, mOn)
			else:
				return(False, 0, 0)
		except:
			print("Could not read telegram")
	
	def getTimeOff(data):
		data = data.decode()
		try:
			command = data.split(" ")
			if tOff in command:
				temp = command[command.index(tOff) + 1]
				temp = temp.split(":")
				hOff = temp[0]
				mOff = temp[1]
				print("mottat tid Off: ", hOff, ":", mOff)
				return(True, hOff, mOff)
			else:
				return(False, 0, 0)
		except:
			print("Could not read telegram")

	def getMode(data):
		data = data.decode()
		try:
			command = data.split(" ")
			if mode in command:
				return(True, command[command.index(mode) + 1])
			else:
				return(False, 0)
		except:
			print("Could not read telegram")
