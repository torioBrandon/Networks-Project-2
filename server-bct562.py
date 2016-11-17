#Brandon Torio 
#bct562
#networks Project 2

from socket import * 
import time
import os.path
import sys
import datetime
import ipaddress
#import ipnetwork

serverName = 'localhost'
serverPort = int(sys.argv[1])

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

#server can receive messages updating ruoting information 
#server can receive questions asking where it would route a message
#this is a dict of lists
rtable = {'A' : ['0.0.0.0', 99], 
		  'B' : ['0.0.0.0', 99], 
		  'C' : ['0.0.0.0', 99], 
		  'D' : ['0.0.0.0', 99],
		  'E' : ['0.0.0.0', 99],
		  'F' : ['0.0.0.0', 99],
		  'G' : ['0.0.0.0', 99],
		  'H' : ['0.0.0.0', 99]
		  }

#rtable = []

def parse_message(input):

	words = input.split()
	print(words)

	if(words[0] == "UPDATE"):
		print("it's an update")
		perform_update(words)

	if(words[0] == "QUERY"):
		print("it's a query")
		perform_query(words)
		#answer the query
	

	return 

def perform_update(words):
	#example of update 
	# UPDATE <cr><lf>
	# A<sp>200.34.55.0/24<sp>22<cr><lf>
	# A<sp>200.34.56.0/24<sp>22<cr><lf>
	# B<sp>200.34.54.0/24<sp>35<cr><lf>
	# C<sp>200.34.0.0/16<sp>41<cr><lf>
	# END<cr><lf>
	
	#iterate over the input, update rtable accordingly 
	i = 1
	#print(len(words))
	while i < (len(words) - 2):
		rtable[words[i]] += [words[i+1], words[i + 2]]
		#print(i)
		i += 3
	print (rtable)
	response = "ACK\r\n"
	response += "END\r\n"
	print(response)
	connectionSocket.send(response.encode())

	return 

def perform_query(words):
	ip = ipaddress.ip_address(words[1])
	weight = 0

	print(rtable)
	for router in rtable:
		i = 0
		while i < len(router):
			#if ip address is in this subnet
			print(router[i])
			ipNet = ipaddress.ip_network((rtable[router])[0])
			if(ip in ipNet):
				print("the ip address is in subnet" + ipNet)
				if(rtable[router[i + 1]] < weight):
					weight = rtable[router[i + 1]]
			i += 2


	return


while 1:
	connectionSocket, addr = serverSocket.accept()
	sentence = connectionSocket.recv(2048)
	sentence = str(sentence.decode())
	parse_message(sentence)
	
	#print(sentence)
	connectionSocket.close()