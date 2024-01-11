# Client
import socket

# Create the socket client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the  serveur
client.connect(('127.0.0.1', 12345))

# Send and receive data
data = client.recv(1024)
print(f'Server says : {data.decode()}')
client.send(b'Hello, server !')

# close the connection
client.close()
