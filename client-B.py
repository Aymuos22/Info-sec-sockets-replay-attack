import socket
import threading

# Connect to the server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('YOUR_SERVER_IP', 9999))  # Replace 'YOUR_SERVER_IP' with the server's local IP address

# Function to receive messages from the server
def receive_from_server():
    while True:
        data = client.recv(4096).decode()
        print("Message received from server:", data)

# Start a thread to receive messages from the server
receive_thread = threading.Thread(target=receive_from_server)
receive_thread.start()

# Input code from the user
code = input("Enter your Python code:\n")

# Send code to the server
client.sendall(code.encode())

# Close the connection
client.close()
