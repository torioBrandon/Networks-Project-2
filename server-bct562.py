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
#this is a dict of lists
rtable = {'A' : [], 
		  'B' : [], 
		  'C' : [], 
		  'D' : [],
		  'E' : [], 
		  'F' : [],
		  'G' : [],
		  'H' : []
		  }

#rtable = []

def parse_message(input):

	words = input.split()
	print(words)

	if(words[0] == "UPDATE"):
		print("it's an update")
		perform_update(input)

	if(words[0] == "QUERY"):
		print("it's a query")
		#answer the query
	

	return 

def perform_update(input):
	#example of update 
	# UPDATE <cr><lf>
	# A<sp>200.34.55.0/24<sp>22<cr><lf>
	# A<sp>200.34.56.0/24<sp>22<cr><lf>
	# B<sp>200.34.54.0/24<sp>35<cr><lf>
	# C<sp>200.34.0.0/16<sp>41<cr><lf>
	# END<cr><lf>
	
	#iterate over the input
	for word in input:
		rtable[input[1]] = [input[1]]

	response = "ACK\r\n"
	response += "END\r\n"
	
	connectionSocket.send(response)

	return 

def receive_query():

	return


while 1:
	connectionSocket, addr = serverSocket.accept()
	sentence = connectionSocket.recv(2048)
	parse_message(sentence)
	
	#print(sentence)
	connectionSocket.close()