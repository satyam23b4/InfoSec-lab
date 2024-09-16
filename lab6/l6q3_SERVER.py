import socket
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization

def diffie_hellman_server():
    # Generate Diffie-Hellman parameters and private key for server
    parameters = dh.generate_parameters(generator=2, key_size=2048, backend=default_backend())
    private_key_server = parameters.generate_private_key()
    public_key_server = private_key_server.public_key()

    # Serialize the public key to send to the client
    public_key_server_bytes = public_key_server.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    # Set up the server socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 9999))
    server_socket.listen(1)
    print("Server listening for client connection...")

    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")

    # Send server's public key to client
    conn.send(public_key_server_bytes)

    # Receive client's public key
    client_public_key_bytes = conn.recv(1024)
    client_public_key = serialization.load_pem_public_key(client_public_key_bytes, backend=default_backend())

    # Generate shared secret
    shared_key_server = private_key_server.exchange(client_public_key)
    print(f"Server's shared secret: {shared_key_server.hex()}")

    conn.close()

# Run the Diffie-Hellman server
diffie_hellman_server()
