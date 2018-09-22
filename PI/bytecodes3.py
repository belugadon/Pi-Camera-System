import camfunct3
#import motion_control

def decode(function_code, argument_code):
	if function_code == b'00':
		camfunct3.demo_preview(float(argument_code[0]))
	elif function_code == b'01':
		camfunct3.brightness(int(argument_code[0]))
	elif function_code == b'02':	
		camfunct3.demo_capture_image(argument_code[0])
	elif function_code == b'03':
		camfunct3.demo_record(float(argument_code[0]), argument_code[1])
	elif function_code == b'04':
		camfunct3.sharpness(int(argument_code[0]))
	elif function_code == b'05':
		camfunct3.contrast(int(argument_code[0]))
	elif function_code == b'06':
		camfunct3.saturation(int(argument_code[0]))
	elif function_code == b'07':
		camfunct3.ISO(int(argument_code[0]))
	elif function_code == b'08':
		camfunct3.rotation(int(argument_code[0]))	
	elif function_code == b'09':
		camfunct3.cam_enable()
	elif function_code == b'10':
		camfunct3.cam_disable()
	elif function_code == b'11':	
		camfunct3.LED(argument_code[0])
	elif function_code == b'12':
		camfunct3.record_loop(float(argument_code[0]), int(argument_code[1]))
	elif function_code == b'13':	
		rotation_pointer = camfunct3.rotation(argument_code[0])
	elif function_code == b'14':
		camfunct3.client(argument_code[0])
	elif function_code == b'15':	
		camfunct3.sleep(float(argument_code[0]))
	elif function_code == b'16':	
		camfunct3.capture_image()
	#elif function_code == b'17':
	#	motion_control.servo_control(int(argument_code[0]))
	#elif function_code == b'18':
	#	motion_control.motor_control(int(argument_code[0]), argument_code[1])
	#elif function_code == b'19':
	#	motion_control.motor_B_control(int(argument_code[0]), argument_code[1])
	elif function_code == b'20':
		pass


	
