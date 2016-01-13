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

# from JourneymanActivities.py
'''1.3) Write a python script which connects to the included server 
on port 50001 and returns the message it receives.'''
# returns the message sent by the server
def journeyman3():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('127.0.0.1', 50001))
    received_string = s.recv(1024)
    s.close()
    return received_string

# from JourneymanString.py (THIS IS THE SERVER)
# it sends the contents of variable message_list
def main():
    HOST  = ''
    PORT  = 50001    
    message_list = ['alpha' , 'bravo' , 'charlie' , 'delta']
    
    for i in message_list:
        s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
        s.bind((HOST , PORT))
        s.listen(1)
        conn, addr = s.accept()
        conn.send(i)
        conn.close()
        
main()

# from JourneymanAvtivitiesTester.py
# compares if the message_list in journeymantest3() is equal with the message in def main in JourneymanString.py
def journeymantest3():
    message_list = ['alpha' , 'bravo' , 'charlie' , 'delta']
    
    for i in message_list:
        res = journeyman3()
        if res != i:
            print "Failed: %s != %s" % (res , i)
            return -1
        print res
    print "Test 3: SUCCESS\n"