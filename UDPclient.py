import socket
import time

# Constants
PORT = 37 # Example port number
SERVER_ADDRESS = ('localhost', PORT)

# Create UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("UDP Client sending request to server")

try:
    # Send request to server
    client_socket.sendto(b'', SERVER_ADDRESS)

    # Receive time from server
    data, addr = client_socket.recvfrom(1024)
    print("UDP Client received data from", addr, ":", data)

    # Convert byte data to integer representing time
    received_time = int.from_bytes(data, 'big')

    # Subtract 2208988800 to get time since 1970
    received_time -= 2208988800

    # Print formatted time
    print("UDP Client received time:", time.ctime(received_time))

except Exception as e:
    print("Error:", e)

finally:
    # Close connection
    client_socket.close()
