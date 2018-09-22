def decode(function_code):
	if function_code == '00':
		print("Command code:{} - demo_preview".format(function_code))
	elif function_code == '01':
		print("Command code:{} - brightness".format(function_code)) 
	elif function_code == '02':
		print("Command code:{} - demo_capture_image".format(function_code))
	elif function_code == '03':
		print("Command code:{} - demo_record".format(function_code))
	elif function_code == '04':
		print("Command code:{} - sharpness".format(function_code))
	elif function_code == '05':
		print("Command code:{} - contrast".format(function_code))
	elif function_code == '06':
		print("Command code:{} - saturation".format(function_code))
	elif function_code == '07':
		print("Command code:{} - ISO".format(function_code))
	elif function_code == '08':
		print("Command code:{} - rotation".format(function_code))
	elif function_code == '09':
		print("Command code:{} - cam_enable".format(function_code))
	elif function_code == '10':
		print("Command code:{} - cam_disable".format(function_code))
	elif function_code == '11':
		print("Command code:{} - LED".format(function_code))
	elif function_code == '12':
		print("Command code:{} - record_loop".format(function_code))
	elif function_code == '13':
		print("Command code:{} - rotation".format(function_code))
	elif function_code == '14':
		print("Command code:{} - streaming".format(function_code))
	else:
		print("Command code:{} - Unknown Command".format(function_code))