###############################
# server1 = listener/receiver #
###############################

import socket
########
# MK2: #
########
def teststorage():
	storage = []



def receive():
	HOST = '127.0.0.1'
	PORT = 50000
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((HOST, PORT))
	receive_string = s.recv(1024)
	s.close()
	return receive_string

def main():
	HOST = ''
	PORT = 50000
	
	for i in range(2):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.bind((HOST, PORT))
		sock.listen(1)
		conn, addr = sock.accept()
		message_received = conn.recv(1024)
		print message_received
		conn.close()
		sock.close()

main()

########
# MK1: #
########
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# socket.AF_INET -> IPv4
# socket.SOCK_STREAM -> TCP
# print "created socket: " , sock 
# HOST = '' # bind every interface(IP addr) of the machine
# PORT = 50000
# sock.bind((HOST, PORT))
# print 'HOST: ', type(HOST)
# print 'PORT: ', PORT
# print 'binding sock.bind((HOST, PORT))'
# sock.listen(1) # waiting for 1 client/connection
# print 'Listening for 1 Client in sock.listen(1):.... '
# conn, addr = sock.accept() # conn -> socket from server2, addr -> IP add and port of server2
# print 'Connection established in: ', conn
# print 'Client IP: ', addr[0],' Client PORT: ', addr[1] 
# message_received = conn.recv(1024)
# print message_received
# print len(message_received)

# for i in message_received:
# 	print i
# conn.close()
# sock.close()