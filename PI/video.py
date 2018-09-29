#!/usr/bin/python
import time
import picamera
import sys
import socket
import datetime
import subprocess
import os

camera = picamera.PiCamera()

def stream(DHCP_add):
        client_socket = socket.socket()
	client_socket.connect((DHCP_add, 8000))

	connection = client_socket.makefile('wb')
	try:
		camera.rotation = 180
		camera.resolution = (640, 480)
		camera.framerate = 24

		camera.start_preview()
		time.sleep(2)

		camera.start_recording(connection, format='mjpeg')
		while True:
                    time.sleep(1)
	finally:
		camera.stop_recording()
		camera.stop_preview()
		connection.close()
		client_socket.close()
		
if __name__=="__main__":
	stream(sys.argv[1])
