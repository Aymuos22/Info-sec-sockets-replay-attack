import socket

# Connect to the server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('YOUR_SERVER_IP', 9999))  # Replace 'YOUR_SERVER_IP' with the server's local IP address

# Input message to send to Client B
message = input("Enter message to send to Client B:\n")

# Send message to the server to forward to Client B
client.sendall(message.encode())

# Close the connection
client.close()
