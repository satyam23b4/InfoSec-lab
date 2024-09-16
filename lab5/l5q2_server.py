import socket


def custom_hash_function(input_string):
    hash_value = 5381
    for char in input_string:
        hash_value = ((hash_value << 5) + hash_value) + ord(char)
        hash_value = hash_value & 0xFFFFFFFF
    return hash_value


# Server code
def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 9999))
    server_socket.listen(1)

    print("Server is listening for connections...")
    conn, addr = server_socket.accept()

    print(f"Connected by {addr}")
    data = conn.recv(1024).decode('utf-8')
    print(f"Received data: {data}")

    # Compute hash of received data
    data_hash = custom_hash_function(data)

    # Send back the computed hash
    conn.send(str(data_hash).encode('utf-8'))
    conn.close()


server()
