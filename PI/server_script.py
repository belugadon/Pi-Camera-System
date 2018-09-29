 #!/usr/bin/env python

import socket
import bytecodes3
import camfunct3


TCP_IP = '0.0.0.0'
TCP_PORT = 5005
BUFFER_SIZE = 1024  # Normally 1024, but we want fast response

def get_packet():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	s.bind((TCP_IP, TCP_PORT))
	s.listen(1)

	conn, addr = s.accept()
	print("Connection address: {}".format(addr))
	data = conn.recv(BUFFER_SIZE)
	conn.send(data)  # echo
	conn.close()
	#TCP_PORT = TCP_PORT + 1
	return str(data)

def main():
	command_code = 0
	while command_code != '99':
		recv_string = get_packet().rstrip("'").lstrip("b'")
		print("received data: {}".format(recv_string))
		message = recv_string.split(":")
		print("Message:")
		command_code = message[0]
		message.pop(0)
		print("command code: {}\n".format(command_code))
		a=0
		for num in message:
			print("argument{0}:{1}".format(a, num))
			a=a+1
		bytecodes3.decode(command_code, message)

if __name__ == "__main__":
	#while True:
	main()
