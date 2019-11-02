from socket import *
import sys
import argparse
# serverName = "localhost"
# serverPort = 12008
# clientSocket = socket(AF_INET, SOCK_STREAM)
# clientSocket.connect((serverName,serverPort))
#sentence = raw_input("Input lowercase sentence:")


def my_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("scpos", help = "something")
    parser.add_argument("-r", "--recurse", help = "recurse")
    parser.add_argument("-e", "--exclude", help = "exclude")
    args = parser.parse_args()
    if args.scpos == "scpos":
        print("you made it! scpos works")
    if args.recurse == "recurse":
        print("yay again! recurse works")
    if args.exclude == "exclude":
        print("woohooooo, exlude works")

my_parser()

# clientSocket.send(sentence)
# modifiedSentence = clientSocket.recv(1024)
# print "From Server:", modifiedSentence
# clientSocket.close()
