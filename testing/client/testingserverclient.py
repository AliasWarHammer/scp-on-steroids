from socket import *
import sys
import argparse
serverName = "localhost"
serverPort = 12008
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))




command = "get"
filepath = "serverfolder"
option = "-r"
sentence = " ".join([command, filepath, option])
print(sentence)
clientSocket.send(sentence.encode())
clientSocket.close()

