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

#server can receive messages updating routing information 
#server can receive questions asking where it would route a message
#routing table:
rtable = {'A' : ['0.0.0.0', 99, 0], 
		  'B' : ['0.0.0.0', 99, 0], 
		  'C' : ['0.0.0.0', 99, 0], 
		  'D' : ['0.0.0.0', 99, 0],
		  'E' : ['0.0.0.0', 99, 0],
		  'F' : ['0.0.0.0', 99, 0],
		  'G' : ['0.0.0.0', 99, 0],
		  'H' : ['0.0.0.0', 99, 0]
		  }

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
	recent = 0
	#print(len(words))
	while i < (len(words) - 2):
		rtable[words[i]] += [words[i+1], words[i + 2], recent]
		#print(i)
		recent += 1
		i += 3
	print (rtable)
	response = "ACK\r\n"
	response += "END\r\n"
	print(response)
	connectionSocket.send(response.encode())

	return 

def perform_query(words):
	ip = ipaddress.ip_address(words[1])
	weight = 100
	most_recent = -1
	best_route = "Z"
	longest_prefix = 0
	print(rtable)
	for router in rtable:
		i = 0
		while i < len(rtable[router]) - 2:
			#print(i)
			# print(len(rtable[router]))
			#if ip address is in this subnet
			ipNet = ipaddress.ip_network((rtable[router])[i])
			#print("comparing ip address " + str(ip) + " to " + str(ipNet))
			if(ip in ipNet):
				# print("the ip address is in subnet " + str(ipNet) + "\n")
				if(int((rtable[router])[i + 1]) <= int(weight)):
					if(longest_prefix < ipNet.prefixlen):
						longest_prefix = ipNet.prefixlen
						weight = rtable[router][i + 1]
						best_route = str(router)
				# if(int((rtable[router])[i + 1]) < int(weight)):
				# 	# if(longest_prefix < ipNet.prefixlen):
				# 		longest_prefix = ipNet.prefixlen
				# 		weight = rtable[router][i + 1]
				# 		best_route = str(router)
				# else: 
				# 	if(int((rtable[router])[i + 1]) == int(weight)):
				# 		if(longest_prefix < ipNet.prefixlen):
				# 			longest_prefix = ipNet.prefixlen
				# 			weight = rtable[router][i + 1]
				# 			best_route = str(router)
				# 		else: 
				# 			if((rtable[router])[i + 2] > most_recent):
				# 				weight = rtable[router][i + 1]
				# 				best_route = str(router)
				# 				most_recent = (rtable[router])[i + 2]
			i += 3

	if(best_route == "Z"):
		best_route = "A"
	response = "RESULT\r\n"
	response += str(ip)
	response += " " + best_route + " " + str(weight) + "\r\n"
	response += "END\r\n"
	print(response)
	connectionSocket.send(response.encode())
	return


while 1:
	connectionSocket, addr = serverSocket.accept()
	sentence = connectionSocket.recv(2048)
	sentence = str(sentence.decode())
	parse_message(sentence)
	
	#print(sentence)
	connectionSocket.close()