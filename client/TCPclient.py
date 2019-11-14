from socket import *
import os
import sys
import argparse

from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

pr_key = RSA.import_key(open('private_pem.pem', 'r').read())
pu_key = RSA.import_key(open('public_pem.pem', 'r').read())
print(type(pr_key), type(pu_key))
decrypt = PKCS1_OAEP.new(key=pr_key)

def my_parser():
    commandList = ["get", "post"]
    if sys.argv[1]=="-h":
        with open('help.txt') as f:
             read_data = f.read()
             print(read_data)
        f.close()
        return 0,0,0
    if sys.argv[1] in commandList:
        if sys.argv[1]=="get":
            if len(sys.argv)==4:
                option = sys.argv[3]
            else: 
                option = ""
            command = "get"
            fileName = sys.argv[2]
            return command, fileName, option

serverName = "localhost"
serverPort = 12008
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

command, fileName, option = my_parser()
if command==0:
    exit(0)
else:
    print(command, fileName, option)
sentence = " ".join([command, fileName, option])
clientSocket.send(sentence.encode())

# key = clientSocket.recv(1024)
# f = Fernet(key)

if option == "-r":
    try:
        with open(fileName+".zip", "wb") as fw:
            while True:
                print('Receiving...')
                # data = f.decrypt(clientSocket.recv(1024))
                data = decrypt.decrypt(clientSocket.recv(1024))
                if not data:
                    break
                fw.write(data)
            fw.close()
            print("Received\n")
            os.system("mkdir "+fileName)
            print("Unzipping...", "unzip ./"+fileName+".zip"+" -d "+fileName)
            os.system("unzip ./"+fileName+".zip"+" -d "+fileName)
            os.system("rm -rf "+fileName+".zip")
            print("")
    except:
        pass
else:
    try:
        with open(fileName, "wb") as fw:
            while True:
                print('Receiving...')
                data = decrypt.decrypt(clientSocket.recv(1024))
                # data = f.decrypt(clientSocket.recv(1024))
                # data = clientSocket.recv(1024)
                if not data:
                    break
                fw.write(data)
            fw.close()
            print("Received\n")
    except:
        pass
clientSocket.close()