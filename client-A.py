import socket

# Connect to the server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('YOUR_SERVER_IP', 9999))  # Replace 'YOUR_SERVER_IP' with the server's local IP address

# Input code from the user
code = input("Enter your Python code:\n")

# Send code to the server
client.sendall(code.encode())

# Close the connection
client.close()
