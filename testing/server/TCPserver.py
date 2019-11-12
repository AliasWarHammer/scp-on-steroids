import os
import daemon
from socket import *

def myrecurse(connectionSocket, filepath):
	try:
		onlyfiles = [f for f in os.listdir(filepath) if os.path.isfile(os.path.join(filepath, f))]
	except:
		pass


def filetransfer(connectionSocket, filename):
	try:
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
	except:
		pass

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
				filetransfer(connectionSocket, filename)
			elif option == '-r':
				myrecurse(connectionSocket, filename)
		elif request[0] == "post":
			try:
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
			except:
				pass
		connectionSocket.close()