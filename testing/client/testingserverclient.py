from socket import *
import os
import sys
import argparse


def my_parser():
    commandList = ["get", "post"]
    if sys.argv[1]=="-h":
        with open('help.txt') as f:
             read_data = f.read()
             print (read_data)
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
# command = "get"
# fileName = "serverfolder"
# option = "-r"
sentence = " ".join([command, fileName, option])
clientSocket.send(sentence.encode())

try:
    with open(fileName+".zip", "wb") as fw:
        print("Receiving..")
        while True:
            print('receiving')
            data = clientSocket.recv(1024)
            # print('Received: ', data.decode('utf-8'))
            if not data:
                print('Breaking from file write')
                break
            fw.write(data)
            # print('Wrote to file', data.decode('utf-8'))
        fw.close()
        print("Received..")
        os.system("mkdir "+fileName)
        print("Unzipping...", "unzip ./"+fileName+".zip"+" -d "+fileName)
        os.system("unzip ./"+fileName+".zip"+" -d "+fileName)
        os.system("rm -rf "+filename+".zip")
except:
    pass
clientSocket.close()