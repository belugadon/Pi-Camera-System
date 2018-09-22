from Tkinter import *    
import serial
import client
import sys
import glob
#import socket
import subprocess
import os
import network
import socket

TCP_IP = ''

class application(Frame):
	cam_angle = 10

	def __init__(self, master):
		Frame.__init__(self, master)
		self.grid()
		self.com()
		self.settings()
		self.files()
		self.demo_on_off()
		
	def settings(self):
		Settings = Label(self, text='Settings')
		Settings.grid(row=0, column=3, columnspan=6, rowspan=3, sticky='NW', padx=0, pady=5, ipadx=0, ipady=5)

		column2 = Label(self)
		column2.grid(row=0, column=2, columnspan=1, sticky='NW', padx=0, pady=0, ipadx=0, ipady=0)

		Settings2 = Label(self, text='Settings2')
		Settings2.grid(row=5, column=2, columnspan=1, rowspan=3, sticky='NW', padx=0, pady=5, ipadx=0, ipady=5)

		#for name, label in [("scale0", "Brightness"), ("scale1", "Sharpness"), ("scale2", "Contrast"), ("scale3", "Saturation")]:
		self.scale0 = Scale(Settings, label="Brightness", from_=100, to=0) 
		self.scale0.pack(side=LEFT)
		self.scale0.set(50)

		self.scale1 = Scale(Settings, label="Sharpness", from_=100, to=0) 
		self.scale1.pack(side=LEFT)
		self.scale1.set(50)

		self.scale2 = Scale(Settings, label="Contrast", from_=100, to=0) 
		self.scale2.pack(side=LEFT)
		self.scale2.set(50)

		self.scale3 = Scale(Settings, label="Saturation", from_=100, to=0) 
		self.scale3.pack(side=LEFT)
		self.scale3.set(50)

		self.scale4 = Scale(Settings, label="ISO", from_=800, to=0) 
		self.scale4.pack(side=LEFT)
		self.scale4.set(50)

		self.shutter_speed = Scale(Settings2, label="Shutter Speed", from_=6000000, to=10000) 
		self.shutter_speed.pack(side=LEFT)
		self.shutter_speed.set(33000)
		
		self.button4 = Button(column2, text="Export to Camera", command=self.export, bg="grey")
		self.button4.pack(side=TOP, anchor=N, ipady=2, ipadx=7, pady=3)

		Stream = Button(column2, text="Stream", command=self.server, bg="grey")
		Stream.pack(side=TOP, ipadx=33, pady=8, anchor=N)

		stop = Button(column2, text="Stop", command=self.disconnect, bg="grey")
		stop.pack(side=TOP, ipadx=40, pady=8, anchor=N)

	def clockwise(self):
		dir1 = []
		dir1.append('>')
		client.transfer_message(TCP_IP, '13', '1', dir1)
		pass

	def counterclockwise(self):
		dir2 = []
		dir2.append('<')
		client.transfer_message(TCP_IP, '13', '1', dir2)
		pass

	def pan_cam_up(self):
		dir1 = []
		application.cam_angle = application.cam_angle-1
		if application.cam_angle < 10:
			application.cam_angle = 10
		dir1.append(str(application.cam_angle))
		client.transfer_message(TCP_IP, '17', '1', dir1)

	def pan_cam_down(self):
		dir2 = []
		application.cam_angle = application.cam_angle+1
		if application.cam_angle > 20:
			application.cam_angle = 20
		dir2.append(str(application.cam_angle))
		client.transfer_message(TCP_IP, '17', '1', dir2)

	def export(self):
		arguments=[]
		bright_value = str(self.scale0.get())
		arguments.insert(0, bright_value)
		client.transfer_message(TCP_IP, '01', '1', arguments)
		print("Brightness: {}".format(bright_value))	
	
		sharpness_value = str(self.scale1.get())
		arguments.insert(0, sharpness_value)
		client.transfer_message(TCP_IP, '04', '1', arguments)
		print("Sharpness: {}".format(sharpness_value))

		contrast_value = str(self.scale2.get())
		arguments.insert(0, contrast_value)
		client.transfer_message(TCP_IP, '05', '1', arguments)
		print("Contrast: {}".format(contrast_value))
	
		saturation_value = str(self.scale3.get())
		arguments.insert(0, saturation_value)
		client.transfer_message(TCP_IP, '06', '1', arguments)
		print("Saturation: {}".format(saturation_value))

		ISO_value = str(self.scale4.get())
		arguments.insert(0, ISO_value)
		client.transfer_message(TCP_IP, '07', '1', arguments)
		print("ISO: {}".format(ISO_value))

		#exposure = str(self.shutter_speed.get())
		#arguments.insert(0, exposure)
		#client.transfer_message(TCP_IP, '21', '1', arguments)
		#print("Exposure: {}".format(exposure))		
	
	def com(self):
		serial_con = Label(self)
		serial_con.grid(column=0, columnspan=2, row=0, sticky='NW', padx=0, pady=0, ipadx=0, ipady=0)
		
		#Stream = Label(self)
		#serial_con.grid(row=1, column=0, columnspan=1, sticky='NW', padx=0, pady=5, ipadx=0, ipady=5)
		
		self.port_list = StringVar(serial_con)
		self.port_list.set("Choose COM Port")
		
		#Connect = Button(serial_con, text="Connect", command=self.assign_port, bg="grey")
		#Connect.pack(side=TOP, ipadx=38, pady=6, anchor=N)

	def server(self):
		arguments=[]
		#network.stream(TCP_IP)
		subprocess.Popen("python network.py {}".format(TCP_IP))
		
	def disconnect(self):
		arguments=[]
		client.transfer_message(TCP_IP, '20', '0', arguments)

	def files(self):
		Buttons = Label(self)
		Buttons.grid(row=1, column=2, sticky='NW', padx=0, pady=0, ipadx=0, ipady=0)

		Fourms = Label(self)
		Fourms.grid(row=1, column=3, columnspan=2, sticky='W', padx=0, pady=0, ipadx=0, ipady=0)
		
		#save = Button(Buttons, text="Save Image As", command=self.capture_image, bg="grey")
		#save.pack(side=TOP, anchor=NE)
		#form2 = Entry(Fourms)
		#form2.pack(side=TOP, anchor=NW, ipady=2, pady=1)
		
		load = Button(Buttons, text="Load Automation File", command=self.load_command_file, bg="grey")
		load.pack(side=LEFT, anchor=N, pady=2)

		self.form3 = Entry(Fourms)
		self.form3.pack(side=LEFT, anchor=W, ipady=2, pady=3)

	def capture_image(self):
		arguments=[]
		exposure = str(self.shutter_speed.get())
		arguments.insert(0, socket.gethostbyname(socket.gethostname()))
		arguments.insert(1, exposure)
		client.transfer_message(TCP_IP, '16', '0', arguments)
		print("Exposure: {}".format(exposure))
		#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		#s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		#s.bind((TCP_IP, 5005))
		#s.listen(1)
		#conn, addr = s.accept()
		#print("Connection address: {}".format(addr))
		#conn.setblocking(0)
		#ready = select.select([conn], [], [], 10)
		#if ready[0]:
                #       data = conn.recv(1024)
                #conn.close()
                #print(data)

	def load_command_file(self):
		arg_list = []
		filename3 = str(self.form3.get())
		command_name = open(filename3, "r+")
		while True:
			command = command_name.readline().rstrip()
			#print("{}".format(command))
			if command == '':
				break
			no_of_arg = command_name.readline().rstrip()
			#print("{}".format(no_of_arg))
			for num in range(0, int(no_of_arg)):
				arg = command_name.readline()
				arg_list.append(arg.rstrip())
			client.transfer_message(TCP_IP, command, no_of_arg, arg_list)
			arg_list.clear()
                                
	def demo_on_off(self):
		Control = Label(self)
		Control.grid(row=0, column=10, sticky='N', padx=0, pady=10, ipadx=0, ipady=0)

		save = Label(self)
		save.grid(row=1, column=10, columnspan=2, sticky='N', padx=0, pady=0, ipadx=0, ipady=0)
		
		pan = Label(self)
		pan.grid(row=0, column=11, sticky='E', padx=0, pady=0, ipadx=0, ipady=0)
				
		self.button1 = Button(Control, text = "Start Demo", fg="green",command = self.start_demo, bg="grey")
		self.button1.pack(side=TOP, anchor=N, ipadx=9)
		
		self.button2 = Button(Control, text = "Stop Demo", fg="red", command = self.stop_demo, bg="grey")
		self.button2.pack(side=TOP, ipadx=10, anchor=N)

		save_but = Button(Control, text="Capture Image", command=self.capture_image, bg="grey")
		save_but.pack(side=TOP, anchor=N)

		button13 = Button(save, text="Counterclockwise", command=self.counterclockwise, bg="grey")
		button13.pack(anchor=SW, side=LEFT)

		button12 = Button(save, text="Clockwise", command=self.clockwise, bg="grey")
		button12.pack(anchor=SE, side=LEFT, ipadx=15 )
	
		servo_up = Button(pan, text="Pan Up", command=self.pan_cam_up, bg="grey")
		servo_up.pack(side=TOP, anchor=E, ipadx=17)

		servo_down = Button(pan, text="Pan Down", command=self.pan_cam_down, bg="grey")
		servo_down.pack(side=BOTTOM, anchor=E, ipadx=10)

	def start_demo(self):
		arguments=[]
		client.transfer_message(TCP_IP, '09', '0', arguments)

	def stop_demo(self):
		arguments=[]
		client.transfer_message(TCP_IP, '10', '0', arguments)


if __name__ == "__main__":
	root=Tk()
	root.title("BATARDO LIVE")
	root.geometry("800x290")
	app=application(root)
	TCP_IP = client.find_pi()
	root.mainloop()
