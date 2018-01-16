import socket
import time

def connetti():
	global clientsocket
	clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	clientsocket.settimeout(60)
	connessione='1'
	while connessione!=None:
		try:
			connessione=clientsocket.connect(('10.1.9.5', 8089))
		except:
			time.sleep(5)
			print ('...CONNESSIONE IN CORSO...' +str(connessione))
	#print ('CONNESSO'+str(connessione))



connetti()
#INIZIO KEEP ALIVE
clientsocket.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
#clientsocket.setsockopt(socket.SOL_TCP, socket.TCP_KEEPIDLE, 60)
#clientsocket.setsockopt(socket.SOL_TCP, socket.TCP_KEEPCNT, 4)
#clientsocket.setsockopt(socket.SOL_TCP, socket.TCP_KEEPINTVL, 15)
#FINE KEEP ALIVE

while 1:
	messaggio=input("->").encode()
	clientsocket.send(messaggio)
	buf = clientsocket.recv(64)
	if len(buf) > 0:
		print(buf.decode()) #DECODIFICA MESSAGGIO
		#break
	