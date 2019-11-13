import os
import hashlib
# import daemon
from socket import *

def myrecurse_zip(connectionSocket, filepath):
	hashed = "temp"
	os.system("zip -r "+"./"+hashed+" "+filepath)
	filetransfer(connectionSocket, "./"+hashed+".zip")
	os.system("rm -rf ./"+hashed+".zip")


def filetransfer(connectionSocket, filename):
	try:
		print('Opening ', filename)
		with open(filename, 'ab+') as fa:
			fa.seek(0, 0)
			print("Sending..")
			while True:
				data = fa.read(1024)
				connectionSocket.send(data)
				if not data:
					break
			fa.close()
		print("Sent\n")
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
	print(request)
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
			myrecurse_zip(connectionSocket, filename)
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