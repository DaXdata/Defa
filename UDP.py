#!/usr/bin/env python3
# -*- coding: iso-8859-15 -*-
#Denne klassen har UDP kommunikasjon for både send og motta

#imports
import socket 

#Create class
class UDP:


	def __init__(self,port_recv,port_send):
		self.port_send = port_send
		self.port_recv = port_recv
		self.addr = None
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.sock.bind(('',self.port_recv))

	def recv_udp(self):
		self.data, self.addr = self.sock.recvfrom(100)
				
	def stop(self):
		self.sock.close()

	def send_udp(self,data):
		try:
			self.send_size = self.sock.sendto(data.encode('utf-8'), (self.addr[0], self.port_send))
		finally:
			return self.send_size
