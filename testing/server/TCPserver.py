import os
# import daemon
from socket import *

def myrecurse(connectionSocket, filepath):
	try:
		onlyfiles = [f for f in os.listdir(filepath) if os.path.isfile(os.path.join(filepath, f))]
		for i in onlyfiles:
			if i[0]!='.':
				print(i, end=" ")
		print()
		onlydir = [f for f in os.listdir(filepath) if os.path.isdir(os.path.join(filepath, f))]
		for i in onlydir:
			print("\nFolder ->", i)
			# sendtype = "***folder***"
			# connectionSocket.send(sendtype)
			myrecurse(connectionSocket, os.path.join(filepath, i))
			# endmarker = "***folder_end***"
			# connectionSocket.send(endmarker)
	except:
		pass


def filetransfer(connectionSocket, filename):
	try:
		print('Opening file ', filename)
		sendtype = "***file***"
		connectionSocket.send(sendtype)
		connectionSocket.send(filename)
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
		
		endmarker = "***file_end***"
		connectionSocket.send(endmarker)
	except:
		pass

serverPort = 12008
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(("",serverPort))
serverSocket.listen(1)
print("The server is ready to receive")
while 1:
	connectionSocket, addr = serverSocket.accept()
	request = connectionSocket.recv(1024)
	request = request.decode()
	if len(request.split()) == 3:
		request, filename, option = request.split()
	else:
		request, filename = request.split()
		option = 0

	print(request, filename, option)
	if request == "get":
		if option == 0:
			print("calling filetransfer function\n")
			filetransfer(connectionSocket, filename)
		elif option == "-r":
			print("calling recurse function\n")
			print("\nFolder ->", filename)
			myrecurse(connectionSocket, filename)
	elif request == "post":
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