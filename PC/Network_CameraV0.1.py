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
import numpy

TCP_IP = ''

global total_length
total_length = 820
global total_height
total_height = 430

class application(Frame):
	def __init__(self, master):
		Frame.__init__(self, master)
		self.grid()
		self.com()
		self.files()
		self.demo_on_off()
		
		#define panel layout with row and column dimensions
                self.First_Row = 5
                self.Row_Height = 30
                self.Column_Width = 90
                self.Xgrid=[]
                self.Ygrid=[]
                self.row_No = 1
                self.column_no = 1

                for i in range(0, 16):
                        self.Xgrid.append(self.First_Row+(i*self.Column_Width))
                        self.Ygrid.append(self.First_Row+(i*self.Row_Height))
                
                self.w = Canvas(master, width=800, height=400)
                self.w.configure(bg="grey")


                for (x, y) in zip(self.Xgrid, self.Ygrid): 
                        self.w.create_line(x, self.First_Row, x, (total_height - self.First_Row))
                        self.w.create_line(self.First_Row, y, (total_length - self.First_Row), y)

                self.w.place(x=0, y=0, width=820, height=430)


		self.button1 = Button(master, text = "Start Demo", fg="green",command = self.start_demo, bg="grey")
		self.button1.place(x=(5+ (8*self.Column_Width)), y=(12*self.Row_Height+self.First_Row), width=self.Column_Width, height=self.Row_Height)
		
		self.button2 = Button(master, text = "Stop Demo", fg="red", command = self.stop_demo, bg="grey")
		self.button2.place(x=(5+ (8*self.Column_Width)), y=(13*self.Row_Height+self.First_Row), width=self.Column_Width, height=self.Row_Height)

		save_but = Button(master, text="Capture Image", command=self.capture_image, bg="grey")
		save_but.place(x=5, y=(2*self.Row_Height+self.First_Row), width=self.Column_Width, height=self.Row_Height)
		
		self.stop = Button(master, text="Stop", command=self.disconnect, bg="grey")
		self.stop.place(x=5, y=(3*self.Row_Height+self.First_Row), width=self.Column_Width, height=self.Row_Height)

		self.load = Button(master, text="Automation File", command=self.load_command_file, bg="grey")
		self.load.place(x=5, y=(4*self.Row_Height+self.First_Row), width=self.Column_Width, height=self.Row_Height)

		self.form3 = Entry(master)
		self.form3.place(x=5, y=(5*self.Row_Height+self.First_Row), width=self.Column_Width, height=self.Row_Height)

		self.scale0 = Scale(master, label="Bright.", from_=100, to=0) 
		self.scale0.place(x=(5+ (4*self.Column_Width)), y=self.First_Row, width=self.Column_Width, height=(5*self.Row_Height))
		self.scale0.set(50)

		self.scale1 = Scale(master, label="Sharp.", from_=100, to=0) 
		self.scale1.place(x=(5+ (5*self.Column_Width)), y=self.First_Row, width=self.Column_Width, height=(5*self.Row_Height))
		self.scale1.set(50)

		self.scale2 = Scale(master, label="Contr.", from_=100, to=0) 
		self.scale2.place(x=(5+ (6*self.Column_Width)), y=self.First_Row, width=self.Column_Width, height=(5*self.Row_Height))
		self.scale2.set(50)

		self.scale3 = Scale(master, label="Sat.", from_=100, to=0) 
		self.scale3.place(x=(5+ (7*self.Column_Width)), y=self.First_Row, width=self.Column_Width, height=(5*self.Row_Height))
		self.scale3.set(50)

		self.scale4 = Scale(master, label="ISO", from_=800, to=0) 
		self.scale4.place(x=(5+ (8*self.Column_Width)), y=self.First_Row, width=self.Column_Width, height=(5*self.Row_Height))
		self.scale4.set(200)
		
		self.button4 = Button(master, text="Send Settings", command=self.export, bg="grey")
		self.button4.place(x=(5+(8*self.Column_Width)), y=(5*self.Row_Height+self.First_Row), width=self.Column_Width, height=self.Row_Height)
		
                self.Stream = Button(master, text="Stream", command=self.server, bg="grey")
		self.Stream.place(x=5, y=(0*self.Row_Height+self.First_Row), width=self.Column_Width, height=self.Row_Height)
		
		button12 = Button(master, text="Clockwise", command=self.clockwise, bg="grey")
		button12.place(x=5, y=(8*self.Row_Height+self.First_Row), width=self.Column_Width, height=self.Row_Height)
				
		self.button13 = Button(master, text="Counterclockw.", command=self.counterclockwise, bg="grey")
		self.button13.place(x=5, y=(9*self.Row_Height+self.First_Row), width=self.Column_Width, height=self.Row_Height)

        #def build_button(self.label, self.row, self.column, )
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

	def export(self):
		arguments=[]
		bright_value = str(self.scale0.get())
		arguments.insert(0, bright_value)
		client.transfer_message(TCP_IP, '01', '1', arguments)
		print("Brightness: {}".format(bright_value))
		arguments=[]
	
		sharpness_value = str(self.scale1.get())
		arguments.insert(0, sharpness_value)
		client.transfer_message(TCP_IP, '04', '1', arguments)
		print("Sharpness: {}".format(sharpness_value))
                arguments=[]

		contrast_value = str(self.scale2.get())
		arguments.insert(0, contrast_value)
		client.transfer_message(TCP_IP, '05', '1', arguments)
		print("Contrast: {}".format(contrast_value))
		arguments=[]
	
		saturation_value = str(self.scale3.get())
		arguments.insert(0, saturation_value)
		client.transfer_message(TCP_IP, '06', '1', arguments)
		print("Saturation: {}".format(saturation_value))
		arguments=[]

		ISO_value = str(self.scale4.get())
		arguments.insert(0, ISO_value)
		client.transfer_message(TCP_IP, '07', '1', arguments)
		print("ISO: {}".format(ISO_value))
		arguments=[]

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
		client.transfer_message(TCP_IP, '21', '0', arguments)

	def files(self):
		Buttons = Label(self)
		Buttons.grid(row=1, column=2, sticky='NW', padx=0, pady=0, ipadx=0, ipady=0)

		Fourms = Label(self)
		Fourms.grid(row=1, column=3, columnspan=2, sticky='W', padx=0, pady=0, ipadx=0, ipady=0)
		
		#save = Button(Buttons, text="Save Image As", command=self.capture_image, bg="grey")
		#save.pack(side=TOP, anchor=NE)
		#form2 = Entry(Fourms)
		#form2.pack(side=TOP, anchor=NW, ipady=2, pady=1)

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

	def start_demo(self):
		arguments=[]
		client.transfer_message(TCP_IP, '09', '0', arguments)

	def stop_demo(self):
		arguments=[]
		client.transfer_message(TCP_IP, '10', '0', arguments)


if __name__ == "__main__":
	root=Tk()
	root.title("BATARDO LIVE")
	root.geometry("820x430")
	app=application(root)
	TCP_IP = client.find_pi()
	root.mainloop()
