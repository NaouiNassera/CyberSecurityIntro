import socket

IP = '0.0.0.0'
PORT = 9998

def send_message(message):
    try:
        # Create a socket object and connect to the server
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.connect((IP, PORT))
            # Send the message after encoding to bytes
            client.send(message.encode('utf-8'))
            # Receive a response from the server
            response = client.recv(4096)
            print(f'Received response from server: {response.decode("utf-8")}')
    except ConnectionRefusedError:
        print("[!] Could not connect to the server. Make sure it's running.")
    except Exception as e:
        print(f"[!] An error occurred: {e}")

if __name__ == '__main__':
    print(f'\n--- Enter messages to send to {IP}:{PORT} or type `quit` to exit ---\n')
    while True:
        message = input("Enter a message to send: ")
        if message.lower() == 'quit':  # Ensures "quit" is not sent to the server
            print("Exiting client...")
            break
        send_message(message)
