#!/usr/bin/env python3
# -*- coding: iso-8859-15 -*-
#Denne klassen har UDP kommunikasjon for både send og motta

#imports
import socket 

#Create class
class UDP:


	def __init__(self,port):
		self.port = port
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.sock.bind(('',port))

	def recv_udp(self):
		self.data, self.addr = self.sock.recvfrom(100)
				
	def stop(self):
		self.sock.close()

	def send_udp(self,data):
		try:
			self.sock.sendto(data, (self.addr[0],port))
		finally:
			return True

	def change(self):
		self.sock.close()
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.sock.bind(self.addr)

