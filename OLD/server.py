import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('10.1.9.5', 8089))
serversocket.listen(5) # become a server socket, maximum 5 connections
serversocket.setblocking(0)

clients = [] #ARRAY CLIENT CONNESSI

def i_manage_clients(clients):    #Function to manage clients
    for client in clients:
        client.send('OK CONNESSO'.encode())

while True:
    connection, address = serversocket.accept()
    clients.append(connection)
    i_manage_clients(clients)
    buf = connection.recv(6)
    if len(buf) > 0:
        print(buf.decode()) #DECODIFICA MESSAGGIO
        #break
