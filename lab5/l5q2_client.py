import socket


def custom_hash_function(input_string):
    hash_value = 5381
    for char in input_string:
        hash_value = ((hash_value << 5) + hash_value) + ord(char)
        hash_value = hash_value & 0xFFFFFFFF
    return hash_value


# Client code
def client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 9999))

    data_to_send = "HelloServer"
    client_socket.send(data_to_send.encode('utf-8'))

    # Receive the hash value from the server
    received_hash = client_socket.recv(1024).decode('utf-8')
    client_socket.close()

    # Compute local hash
    local_hash = custom_hash_function(data_to_send)

    # Compare hashes
    if str(local_hash) == received_hash:
        print("Data integrity verified. No corruption detected.")
    else:
        print("Data corruption or tampering detected!")


client()
