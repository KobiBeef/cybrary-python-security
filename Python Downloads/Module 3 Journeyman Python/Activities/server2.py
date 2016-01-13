###########################
# server2 = client/sender #
###########################
# this is conn from server1

import socket
# SENDING MULTIPLE MESSAGES, ex: string/s in a list
HOST = '127.0.0.1'
PORT = 50000
test = {
		'key1': 'value1', 
		'key2': 'value2', 
		'key3': 'value3',
		}
for k in test:
	print k
	print test[k]

#########################################################
# ATTEMPTING to send contents and saving it in a a list #
#########################################################
# put s.connet and s = socket.socket() out side the for loop to send one whole string
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect((HOST, PORT))
for k in test:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((HOST, PORT))
	# incoming = s.send("INCOMING MESSAGE")
	# file_name = s.send(k)
	# file_content = s.send(test[k])
	# s.send("INCOMING MESSAGE")
	# test_file = s.send(k)
	# s.send(k)
	# s.send(k)
	s.send(k)
	# print 'sending:' ,file_name ,'with contents ' ,file_content # apparently this doesnt work to
	# print "Message Sent"
	s.close()

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect((HOST, PORT))
# s.close()


##########################
# ATTEMPTING DOUBLE SEND #
##########################
# for k in test:
	# file_name = s.send(k)
	# file_content = s.send(test[k])
	# print 'sending: file name', file_name, 'with contents ', file_content # apparently this doesnt work
	# print 'sending: %s with contents %s', (file_name, file_content) # apparently this doesnt work to
	# s.close()

	# FINDINGS: can use double send but having problems when using variables of s.send(),
	# gives an  [Errno 10054] An existing connection was forcibly closed by the remote host
	

	###############
	# SINGLE SEND #
	###############
	# file_content = s.send(test[k]) # sends all the values of test{} in a single line
	# print 'file contents are: ',file_content
	# file_name = s.send(k) # this sends all the keys in test{} in a single line
	# print 'file names are: ', file_name
	# k_byte = s.send(k)
	# print 'sending: file ',  ', file contents: ', k_byte # this prints the byte/len of s.send(k)
	# s.close() # closing this would only send 1 test[k] the last test[k]



# BASIC SOCKET CONNECTION
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect(('127.0.0.1', 50000)) # this is PORT of server1 (connecting to server1)
# message_send = s.send('Hello World') # can add raw_input() to send
# print message_send