import socket

def client():
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Get the server IP address and port
    host = socket.gethostname()
    port = 8000
    
    # Connect to the server
    client_socket.connect((host, port))
    
    # Receive the random number from the server
    data = client_socket.recv(1024).decode()
    print('Received random number:', data)
    
    # Close the connection
    client_socket.close()

# Start the client
client()

