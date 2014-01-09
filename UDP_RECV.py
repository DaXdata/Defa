#Denne filen skal inneholde en klasse som kan sende data den f?r inn

import socket #Initialisere UDP adresse og port

class recv:

	def __init__(self,ip,port):
		done = False	
		sock = socket.socket(socket.AF_INET, #Internet
			socket.SOCK_DGRAM) #UDP
		sock.bind((ip, port))

		while not done:
			self.data, self.addr = sock.recvfrom(1024) 
			done = True

		sock.close()

