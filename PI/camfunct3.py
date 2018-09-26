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
#import RPi.GPIO as GPIO
#GPIO.setwarnings(False)

#GPIO.setmode(GPIO.BCM)
#GPIO.setup(4, GPIO.OUT)
#GPIO.output(4, False)

camera = picamera.PiCamera()

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
	subprocess.Popen("python video.py {}".format(DHCP_add))

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

def servo_control(n):
	print("Write {} to servo controller\n".format(n))
	#GPIO.output(4, True)
	#time.sleep(2)
	bus = smbus.SMBus(1)
	DEVICE_ADDRESS = 0x28
	DEVICE_REGISTER = 0xAF
	#time.sleep(2)
	bus.write_byte_data(DEVICE_ADDRESS, DEVICE_REGISTER, n)
	#time.sleep(2)
	#GPIO.output(4, False)
	print("\nturd!")
	#return 0
