import socket
import time

def connetti():
	global clientsocket
	clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	connessione='1'
	while connessione!=None:
		try:
			connessione=clientsocket.connect(('localhost', 8089))
		except:
			time.sleep(5)
			print ('...CONNESSIONE IN CORSO...' +str(connessione))
	#print ('CONNESSO'+str(connessione))

while 1:
	connetti()
	messaggio=input("->")
	clientsocket.sendto(messaggio.encode('utf-8'),('localhost', 8089)) #INVIO CON CODIFICA
	clientsocket.close()
	