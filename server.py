import socket
import threading

# Function to handle client connections
def handle_client(client_socket, client_address, client_id):
    print(f"Connected with client {client_id}: {client_address}")

    # Receive data from the client
    data = client_socket.recv(4096).decode()
    print(f"Received code from client {client_id}:\n{data}")

    # Send received data to the other clients
    for id, other_client_socket in clients.items():
        if id != client_id:
            other_client_socket.sendall(data.encode())

    # Close the connection
    client_socket.close()

# Set up the server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 9999))
server.listen(3)
print("Server listening on port 9999")

# Accept incoming connections
clients = {}
client_id = 1
while True:
    client_socket, client_address = server.accept()
    clients[client_id] = client_socket
    client_handler = threading.Thread(target=handle_client, args=(client_socket, client_address, client_id))
    client_handler.start()
    client_id += 1
