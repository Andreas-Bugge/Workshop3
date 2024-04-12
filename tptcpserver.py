import socket
import time
import sys

# Get current time in seconds since 1900
def get_current_time():
    return int(time.time()) + 2208988800

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Missing port: python .\\tptcpserver.py <port>")
        sys.exit(1)
    PORT = int(sys.argv[1])

    # Create TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the address and port
    server_socket.bind(('', PORT))
    
    # Listen for incoming connections
    server_socket.listen()

    print("Server listening on port", PORT)

    try:
        while True:
            # Accept incoming connection
            client_socket, addr = server_socket.accept()
            print("Server connected to", addr)

            try:
                # Get current time
                current_time = get_current_time()

                # Convert time to 32-bit big-endian byte representation
                current_time_byte = current_time.to_bytes(4, 'big')

                # Send time to client
                client_socket.sendall(current_time_byte)
                print("Server has sent the time:", current_time_byte)

            finally:
                # Close connection
                client_socket.close()
                print("Server has closed connection")

    except KeyboardInterrupt:
        print("\nServer shutting down...")
        server_socket.close()
        sys.exit(0)
