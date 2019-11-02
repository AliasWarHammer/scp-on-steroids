import os
import daemon
from socket import *

with daemon.DaemonContext():
	serverPort = 12008
	serverSocket = socket(AF_INET,SOCK_STREAM)
	serverSocket.bind(("",serverPort))
	serverSocket.listen(1)
	print("The server is ready to receive")
	while 1:
		connectionSocket, addr = serverSocket.accept()
		request = connectionSocket.recv(1024)
		if len(request.split() == 3):
			request, filename, option = request.split()
		else:
			request, filename = request.split()
			option = 0
		if request[0] == "get":
			if option == 0:
				pass
				print('Opening file ', filename)
				with open(filename, 'ab+') as fa:
					print('Opened file')
					fa.seek(0, 0)
					print("Sending file.")
					while True:
						data = fa.read(1024)
						connectionSocket.send(data)
						if not data:
							break
					fa.close()
					print("Sent file.")
			else:
				pass
		if request[0] == "post":
			with open(filename, "wb") as fw:
				print("Receiving..")
				while True:
					print('receiving')
					data = connectionSocket.recv(1024)
					print('Received: ', data.decode('utf-8'))
					if not data:
						print('Breaking from file write')
						break
					fw.write(data)
					print('Wrote to file', data.decode('utf-8'))
				fw.close()
				print("Received..")

		connectionSocket.close()	
