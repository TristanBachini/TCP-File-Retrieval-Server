#import socket module
from socket import *
import sys # In order to terminate the program
serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
#Fill in start
serverSocket.bind(('', 12000))
serverSocket.listen(1)
#Fill in end
while True:
	#Establish the connection
	print('Ready to serve...')
	connectionSocket, addr = serverSocket.accept()
	print(addr)
	try:
		message = connectionSocket.recv(1024)
		filename = message.split()[1]
		f = open(filename[1:])
		outputdata = f.read()
		connectionSocket.sendall(str.encode("""HTTP/1.1 200 OK\n""",'iso-8859-1'))
		connectionSocket.sendall(str.encode("\n"+outputdata+"", 'iso-8859-1'))
		connectionSocket.close()
	except IOError:
		#Send response message for file not found
		#Fill in start
		connectionSocket.sendall(str.encode("""HTTP/1.1 404 Not Found\n""",'iso-8859-1'))
		connectionSocket.sendall(str.encode("\n<h1>Error 404 Not Found<h1>",'iso-8859-1'))
		#Fill in end
		#Close client socket
		#Fill in start
		connectionSocket.close()
		#Fill in end
serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data