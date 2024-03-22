import socket
import time

# Constants
PORT = 37  # Example port number

# Create TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
client_socket.connect(('localhost', PORT))

print("Client connected on port", PORT)

try:
    # Receive time from server
    data = client_socket.recv(4)
    print("Client received data:", data)

    # Convert byte data to integer representing time
    received_time = int.from_bytes(data, 'big')

    # Subtract 2208988800 to get time since 1970
    received_time -= 2208988800

    # Print formatted time
    print("Client received time:", time.ctime(received_time))

finally:
    # Close connection
    client_socket.close()
    print("Client closed connection")
