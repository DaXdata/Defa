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

#################################################
#		    Create class		#
#################################################

class Parse:


	def getTimeOn(data):
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
	
	def getTimeOff(data):
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
