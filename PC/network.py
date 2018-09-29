#import serial
#import serial_talk4
import client
import sys
import socket
import subprocess
import os

#server_socket=0
#connection=0

def stream(TCP_IP):
	arguments=[]
	arguments.insert(0, socket.gethostbyname(socket.gethostname()))
	client.transfer_message(TCP_IP, '14', '1', arguments)
	# Start a socket listening for connections on 0.0.0.0:8000 (0.0.0.0 means
	# all interfaces)
	server_socket = socket.socket()
	server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	server_socket.bind(('0.0.0.0', 8000))
	server_socket.listen(0)

	# Accept a single connection and make a file-like object out of it
	connection = server_socket.accept()[0].makefile('rb')
	try:
    		# Run a viewer with an appropriate command line. Uncomment the mplayer
    		# version if you would prefer to use mplayer instead of VLC
		cmdline = ['vlc.exe', '--demux', 'mjpeg', '-']
		#cmdline = ['mplayer.exe', '-fps', '25', '-cache', '1024', '-']
		player = subprocess.Popen(cmdline, stdin=subprocess.PIPE)
		while True:
			# Repeatedly read 1k of data from the connection and write it to
			# the media player's stdin
			data = connection.read(1024)
			if not data:
				break
			player.stdin.write(data)	
	finally:
		connection.close()
		server_socket.close()
		player.terminate()

if __name__=="__main__":
	stream(sys.argv[1])
