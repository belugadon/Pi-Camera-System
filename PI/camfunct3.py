import time
import picamera
import sys
import serial
import socket
import datetime
import subprocess
import os
import server_script
#import smbus
import RPi.GPIO as GPIO
#GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.OUT)
GPIO.output(20, False)
GPIO.setup(16, GPIO.OUT)
GPIO.output(16, False)
GPIO.setup(23, GPIO.OUT)
GPIO.output(23, False)

camera = picamera.PiCamera()
global client_socket
global connection# = client_socket.makefile('wb')
global client_DHCP_address

def demo_preview(n):
	"""Demo the Pi camera for n seconds
*****************************************************
	"""
	print("Demo the Pi camera for n seconds\n*****************************************************")
	print ("\nCamera will now activate for {} seconds.".format(n))
	camera.start_preview()
	time.sleep(n)
	camera.stop_preview()
	return 0

def demo_record(n, file_name):	
	print("Record n seconds of video.\n*****************************************************")
	print ("\nCamera will now activate for {} seconds.".format(n))
	file = open(file_name, 'wb')
	try:
		camera.resolution = (640, 480)
		camera.start_preview()
		#time.sleep(2)
		camera.start_recording(file_name)
		camera.wait_recording(n)
		camera.stop_recording()
		camera.stop_preview()
	finally:
		file.close()
	return 0

def brightness(n):
	"""Control camera birghtness.
*****************************************************
	"""
	print("control camera brightness\n*****************************************************")	
	camera.brightness = n

def sharpness(n):
	"""Control camera sharpness.
*****************************************************
	"""
	print("control camera sharpness\n*****************************************************")	
	camera.sharpness = n		

def contrast(n):
	"""Control camera contrast.
*****************************************************
	"""
	print("control camera contrast\n*****************************************************")	
	camera.contrast = n		

def saturation(n):
	"""Control camera saturation.
*****************************************************
	"""
	print("control camera saturation\n*****************************************************")	
	camera.saturation = n

def ISO(n):
	"""Control camera ISO.
*****************************************************
	"""
	print("control camera ISO\n*****************************************************")	
	camera.ISO = n

def rotation(n):
	"""Control camera rotation.
*****************************************************
	"""
	print("control camera rotation\n*****************************************************")	
	camera.rotation = n

def cam_enable():
	"""Activate Pi camera
*****************************************************
	"""
	print("Activate Poop camera\n*****************************************************")
	camera.start_preview()
	return 0 

def cam_disable():	
	"""Deactivate Pi camera
*****************************************************
	"""
	print("Deactivate Pi camera\n*****************************************************")
	camera.stop_preview()

def LED(n):
	"""Control camera LED
*****************************************************
	"""
	print("Control camera LED\n*****************************************************")
	camera.led = n

def record_loop(n, a):
	"""if a = 0 loop for infinity
*****************************************************
	"""
	print("Record n seconds of video, a times.\n*****************************************************")
	if a == 0:
		i = 1
		while True:
			try:
				demo_record(n, "/mnt/vid{}.h264".format(i))
				i = i+1
			except (KeyboardInterrupt, SystemExit):
				raise		
	else:
		for num in range(1, a+1):
			print("{}".format(num))
			demo_record(n, "/mnt/vid{}.h264".format(num))

def rotation(ch):
	"""Control camera rotation
*****************************************************
	"""
	print("Control camera rotation\n*****************************************************")
	degrees = [0, 90, 180, 270]
	if ch == '>':
		if camera.rotation == 0:
			camera.rotation = 90
			#break
		elif camera.rotation == 90:
			camera.rotation = 180
			#break
		elif camera.rotation == 180:
			camera.rotation = 270
			#break
		elif camera.rotation == 270:
			camera.rotation = 0
			#break		 
	elif ch == '<':
		if camera.rotation == 0:
			camera.rotation = 270
			#break
		elif camera.rotation == 90:
			camera.rotation = 0
			#break
		elif camera.rotation == 180:
			camera.rotation = 90
			#break
		elif camera.rotation == 270:
			camera.rotation = 180
			#break	

	print("Camera Rotation: {}".format(camera.rotation))

def client(DHCP_add):
        global client_DHCP_address
        client_DHCP_address = DHCP_add
        
def begin_stream():
	global connection
	global client_DHCP_address
	global client_socket
	client_socket = socket.socket()
        client_socket.connect((client_DHCP_address, 8000))
	connection = client_socket.makefile('wb')
	camera.rotation = 180
	camera.resolution = (640, 480)
	camera.framerate = 24
	camera.start_preview()
	time.sleep(2)
	camera.start_recording(connection, format='mjpeg')
	

def end_stream():
    	camera.stop_recording()
	camera.stop_preview()
	connection.close()
	client_socket.close()

def sleep(n):
	time.sleep(n)
	return 0

def capture_image():	
	print("Capture image to file_name.\n*****************************************************")
	#print ("\nCapture will be saved as {}.".format(file_name))
	camera.resolution = (1024, 768)
	camera.start_preview()
	time.sleep(2)
	date=datetime.datetime.now().strftime("%y%m%d%h%m%s")
	camera.capture("/media/pi/F4C0-B15B/Pictures/{}.jpg".format(date))
	camera.stop_preview()

def output(n):
    if n == '1':
        GPIO.output(20, True)
        print ("out 1")
    else:
        GPIO.output(20, False)
    if n == '2':
        GPIO.output(16, True)
        print ("out 2")
    else:
        GPIO.output(16, False)
    if n == '3':
        GPIO.output(23, True)
        print ("out 3")
    else:
        GPIO.output(23, False)
    if n == '4':
        GPIO.output(23, False)
        GPIO.output(20, False)
        GPIO.output(16, False)        
        print ("out off") 
        
