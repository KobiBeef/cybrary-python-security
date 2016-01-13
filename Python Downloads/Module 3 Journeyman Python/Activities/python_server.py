import socket

# PROB:1 TESTING SOCKETS
# TICKET:1 SOCKET CONNECTING

# NEED TO CREATE A LOOP THAT WOULD CONNECT EVERYTIME A MESSAGE IS SENT 
python_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# socket.AF_INET -> IPv4
# socket.SOCK_STREAM -> TCP
print "created socket: " , python_server_socket
HOST = '' # bind every interface(IP addr) of the machine
PORT = 50002
python_server_socket.bind((HOST, PORT))
print 'HOST: ', type(HOST)
print 'PORT: ', PORT
print 'binding sock.bind((HOST, PORT))'
python_server_socket.listen(1) # waiting for 1 client/connection
print 'Listening for 1 Client in sock.listen(1):.... '
conn, addr = python_server_socket.accept() # conn -> socket from server2, addr -> IP add and port of server2
print 'Connection established in: ', conn
print 'Client IP: ', addr[0],' Client PORT: ', addr[1] 
message_received = conn.recv(1024)
for i in message_received:
	print i , '\n'
conn.close()
python_server_socket.close()