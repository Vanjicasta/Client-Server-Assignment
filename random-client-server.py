import random
import socket

def server():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Get the local machine name and choose a port
    host = socket.gethostname()
    port = 8000
    
    # Bind the socket to a specific address and port
    server_socket.bind((host, port))
    
    # Listen for incoming connections
    server_socket.listen(1)
    print('Server listening on {}:{}'.format(host, port))
    
    # Accept a client connection
    client_socket, addr = server_socket.accept()
    print('Connected to client:', addr)
    
    # Generate a random number between 1 and 10
    random_number = random.randint(1, 10)
    print('Random number:', random_number)
    
    # Send the random number to the client
    client_socket.send(str(random_number).encode())
    
    # Close the connection
    client_socket.close()
    server_socket.close()

# Start the server
server()