#!/usr/bin/python3


import socket
import random

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.bind(('localhost', 1234))

mySocket.listen(5)
try:
	while True:
		num_aleatorio = random.randint(1,10000)
		print('Waiting for connections')
		(recvSocket, address) = mySocket.accept()
		print('HTTP request received:')
		html_answer = '<html><body>'
		html_answer += '<h1><a href = ' + str(num_aleatorio) + '>Dame otra</a></h1>' 
		html_answer += '</html></body>'
		
		print(recvSocket.recv(1024))
		recvSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n" + html_answer + '\r\n','utf-8'))
		recvSocket.close()
		
except KeyboardInterrupt:
	print("\nClosing binded socket")
	mySocket.close()
