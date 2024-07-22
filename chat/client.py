import socket
import select
import sys

def client_program():
    if len(sys.argv) != 3:
        print("Correct usage: script, IP address, port number")
        exit()

    IP_address = str(sys.argv[1])
    Port = int(sys.argv[2])

    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to the server
        client_socket.connect((IP_address, Port))
    except Exception as e:
        print(f"Error connecting to the server: {e}")
        exit()

    print("Connected to the chat server. You can start sending messages.")

    while True:
        sockets_list = [sys.stdin, client_socket]

        # Use select to manage input from stdin and server socket
        read_sockets = sockets_list

        for sock in read_sockets:
            if sock == client_socket:
                # Receive message from server
                message = sock.recv(2048).decode()
                if not message:
                    print("Connection closed by server")
                    client_socket.close()
                    return
                else:
                    print(message)
            else:
                # User input from stdin
                message = sys.stdin.readline().strip()  # Strip newline character
                if message.lower() == 'exit':
                    client_socket.close()
                    return
                client_socket.send(message.encode())

if __name__ == '__main__':
    client_program()
