import os
import hashlib
import daemon
from socket import *

from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

pr_key = RSA.import_key(open('private_pem.pem', 'r').read())
pu_key = RSA.import_key(open('public_pem.pem', 'r').read())
print(type(pr_key), type(pu_key))
cipher = PKCS1_OAEP.new(key=pu_key)

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
			print("Sending...")
			while True:
				data = fa.read(1024)
				# data = cipher.encrypt(data)
				connectionSocket.send(data)
				if not data:
					break
			fa.close()
		print("Sent")
	except:
		pass

# with daemon.DaemonContext():
serverPort = 12008
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(("",serverPort))
serverSocket.listen(1)
print("The server is ready...")
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
			filetransfer(connectionSocket, filename)
		elif option == "-r":
			print("\nFolder...", filename)
			myrecurse_zip(connectionSocket, filename)
	elif request == "post":
		try:
			with open(filename, "wb") as fw:
				print("Receiving...")
				while True:
					data = connectionSocket.recv(1024)
					if not data:
						break
					fw.write(data)
				fw.close()
				print("Received")
		except:
			pass
	connectionSocket.close()