#!/usr/bin/python3
from socket import *
import sys
import argparse


def my_parser():
    commandList = ["get", "post"]
    #help option
    if sys.argv[1]=="-h":
        with open('help.txt') as f:
             read_data = f.read()
             print (read_data)
        f.close()
        return 0,0,0
    if sys.argv[1] in commandList:
        if sys.argv[1]=="get":
            # print(sys.argv)
            if len(sys.argv)==4:
                option = sys.argv[3]
            else: 
                option = ""
            command = "get"
            #option = sys.argv[3]
            IP, fileName = sys.argv[2].split(":")
            # print(command)
            # print(fileName)
            # print(option)
            return command, IP,fileName, option
        # if sys.argv[1]=="post":
        #     command = "post"
        #     #option = sys.argv[3]
        #     fileName = sys.argv[2]
        #     print(command)
        #     print(fileName)
        #     print(option)
    

# serverName = "localhost"
# serverPort = 12008
# clientSocket = socket(AF_INET, SOCK_STREAM)
# clientSocket.connect((serverName,serverPort))
command, IP, filenName, option = my_parser()
if command==0:
    exit(0)
else:
    print(command, IP, filenName, option)

#sentence = raw_input("Input lowercase sentence:")
# clientSocket.send(sentence)
# modifiedSentence = clientSocket.recv(1024)
# print(‘From Server:’, modifiedSentence)
# clientSocket.close()
# print('Number of arguments:', len(sys.argv), 'arguments.')
# print('Argument List:', str(sys.argv))

    







# def my_parser():
#     parser = argparse.ArgumentParser(add_help=False)
#     parser.add_argument("scpos")
#     parser.add_argument("-h", "--help")
#     parser.add_argument("-r", "--recurse")
#     parser.add_argument("-e", "--exclude")
#     args = parser.parse_args()
#     if args.scpos == "scpos":
#         print("you made it! scpos works")
#     if args.recurse == "recurse":
#         print("yay again! recurse works")
#     if args.exclude == "exclude":
#         print("woohooooo, exlude works")
#     if args.help == "help":
#         with open('help.txt') as f:
#              read_data = f.read(
#              print (read_data)
#         f.close()
# my_parser()

# clientSocket.send(sentence)
# modifiedSentence = clientSocket.recv(1024)
# print "From Server:", modifiedSentence
# clientSocket.close()
