# chat_client.py

import sys
import socket
import select
 
def chat_client():
	if(len(sys.argv) < 3) :
		print ('Usage : python chat_client.py hostname port')
		sys.exit()

	host = sys.argv[1]
	port = int(sys.argv[2])
	 
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.settimeout(2)
	 
	# connect to remote host
	try :
		s.connect((host, port))
	except :
		print ('Unable to connect')
		sys.exit()
	 
	print ('Connected to remote host. You can start sending messages')
	msg = input("->").encode()
	
	while 1:
		socket_list = [s]
		print ("SONO NEL WHILE")
		# Get the list sockets which are readable
		ready_to_read,ready_to_write,in_error = select.select([s] , [], [])
		print(ready_to_read)
		for sock in ready_to_read:
			print ("SONO NEL FOR ")
			if sock == s:
				print ("SONO NEL FOR - IF")
				# incoming message from remote server, s
				data = sock.recv(4096)
				if not data :
					print ("DISCONNESSO")
					print ('\nDisconnected from chat server')
					sys.exit()
				else :
					print ("STAMPA DATA")
					print(data.decode())
			
			else :
				print ("INPUT")
				# user entered a message
				msg = input("->").encode()
				s.send(msg)


if __name__ == "__main__":

	sys.exit(chat_client())