#Brandon Torio 
#bct562
#networks Project 2

from socket import * 
import time
import os.path
import sys
import datetime
import ipaddress 

serverName = 'localhost'
serverPort = int(sys.argv[1])

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

#server can receive messages updating ruoting information 
#server can receive questions asking where it would route a message

rtable = {'A' : [], 
		  'B' : [], 
		  'C' : [], 
		  'D' : [],
		  'E' : [], 
		  'F' : [],
		  'G' : [],
		  'H' : []
		  }

def parse_message(input):

	words = input.split()
	print(words)

	if(words[0] == "UPDATE"):
		print("it's an update")
		check_update(input)

	if(words[0] == "QUERY"):
		print("it's a query")
		#answer the query
	

	return

def check_update(input):

	#do a bunch of stuff
	return

def receive_query():

	return


while 1:
	connectionSocket, addr = serverSocket.accept()
	sentence = connectionSocket.recv(2048)
	parse_message(sentence)
	#print(sentence)
	connectionSocket.close()