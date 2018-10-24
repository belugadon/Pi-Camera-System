#!/usr/bin/env python

import socket
import bytecodes

pack = []
TCP_PORT = 5005
BUFFER_SIZE = 1024

def transfer_message(TCP_IP, command_code, arg_list, arguments):
	#a=0
	packet = command_code
	for num in arguments:
		packet = packet + ':' + num
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((TCP_IP, TCP_PORT))
	#while data:
	s.send(packet.encode('latin1'))
		#a=a+1
	returned_data = s.recv(BUFFER_SIZE)
	#print("returned data: {}".format(returned_data))
	#a=0
	s.close()

def find_pi():
	print("Scaning the network for the robot")
	a=0
	packet = '20'
	packet = packet + ':' + '0'
	while a <= 254:
		TCP_IP = '192.168.0.{}'.format(a)
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		#print("{}".format(TCP_IP))
		try:
			s.settimeout(.1)
			s.connect((TCP_IP, TCP_PORT))
			#while data:
			s.send(packet.encode('latin1'))
				#a=a+1
			returned_data = s.recv(BUFFER_SIZE)
			print("Connected to:{}".format(TCP_IP))
			#if returned_data:
				#print("returned data: {}".format(returned_data))			 
			s.close()
			break
		except:
			a=a+1
	return TCP_IP

if __name__ == "__main__":
	while True:
		command_code = ""
		command = []
		argument_code = ""
		arguments = []
			
		command_code = input("Input command code:")
		bytecodes.decode(command_code)
		
		while True:
			argument_code = input("Input argument codes:")
			if argument_code == 'x':
				break
			arguments.append(argument_code)
	
		arg_list = str(len(arguments))
		print(command)

		transfer_message(command_code, arg_list, arguments)
