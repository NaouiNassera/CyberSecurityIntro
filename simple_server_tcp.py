import socket
import threading

IP = '0.0.0.0'
PORT = 9998

def main():
    # Create the socket object with IPv4 and TCP
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Set socket option to reuse the address to prevent "Address already in use" errors
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    try:
        # Bind the socket to the specified IP and port
        server.bind((IP, PORT))
        # Start listening for incoming connections, with a backlog of 5
        server.listen(5)
        print(f'[*] Listening on {IP}:{PORT}')

        while True:
            # Accept new connections
            client, address = server.accept()
            print(f'[*] Accepted connection from {address[0]}:{address[1]}')
            
            # Create a new thread to handle the client communication
            client_handler = threading.Thread(target=handle_client, args=(client,), daemon=True)
            client_handler.start()
    
    except Exception as e:
        print(f'[!] Error: {e}')
    finally:
        # Ensure the server socket is properly closed on exit
        server.close()

def handle_client(client_socket):
    try:
        with client_socket as sock:
            # Receive data with a buffer size of 1024 bytes
            request = sock.recv(1024)
            print(f'[*] Received: {request.decode("utf-8")}')
            
            # Send response back to the client
            sock.send(b'200 - OK')
    
    except Exception as e:
        print(f'[!] Error handling client: {e}')

if __name__ == '__main__':
    main()
