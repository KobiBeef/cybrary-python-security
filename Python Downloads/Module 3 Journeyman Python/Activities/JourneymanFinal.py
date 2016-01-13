import socket
'''
1.5) Python Journeyman: Write a Python server which:
	receives a connection from the included client (JourneymanFinal.py)
	stores received data in a file, then adds the file to a list
	returns the data from the file when requested
	deals with errors and missing files
'''

# 1. Python server which receives a connection from JourneymanFinal.py
# 2. JourneymanFinal.py will be the Python server
# 2.5 Python server will be the receiver
# 3. Python server will store received data in a file ( Server Creates the file )
# 4. Python server will add contents of the file to a list
# 5. Pyhotn server returns the data from the list when requested
# 6. Deals with errors and missing files

# 2 main function save() and load()

def save():
	pass
def load():
	pass

def main():
	server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	HOST = ''
	PORT = 50002
	server_sock.bind((HOST, PORT))
	server_sock.listen(1)
	conn, addr = server_sock.accept()
	message_received = conn.recv(1024)
	print message_received
	conn.close()
	server_sock.close()
main()