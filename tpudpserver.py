import socket
import time
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Missing port: python .\\tpudpserver.py <port>")
        sys.exit(1)
    PORT = int(sys.argv[1])
# Constants
#PORT = 37  # Example port number

# Get current time in seconds since 1900
def get_current_time():
    return int(time.time()) + 2208988800

# Create UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the address and port
server_socket.bind(('localhost', PORT))

print("UDP Server listening on port", PORT)

while True:
    # Receive request from client
    data, addr = server_socket.recvfrom(1024)
    print("UDP Server received request from", addr)

    try:
        # Get current time
        current_time = get_current_time()

        # Convert time to 32-bit big-endian byte representation
        current_time_byte = current_time.to_bytes(4, 'big')

        # Send time to client
        server_socket.sendto(current_time_byte, addr)
        print("UDP Server has sent the time:", current_time_byte)

    except Exception as e:
        print("Error:", e)

    finally:
        sys.exit(1)
