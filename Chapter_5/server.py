# Server
import socket

# Create the socket server
serveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Link the socket to an address and port
serveur.bind(('0.0.0.0', 12345))

# listen to input connections
serveur.listen(5)

while True:
    # Accept the connection
    client, adresse = serveur.accept()
    print(f'Connecting from {adresse}')

    # Send and Receive data
    client.send(b'Welcome to the chat server !')
    data = client.recv(1024)
    print(f'Client says : {data.decode()}')

    # Close the connection
    client.close()