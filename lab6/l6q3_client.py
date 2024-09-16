import socket
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization

def diffie_hellman_client():
    # Generate Diffie-Hellman parameters and private key for client
    parameters = dh.generate_parameters(generator=2, key_size=2048, backend=default_backend())
    private_key_client = parameters.generate_private_key()
    public_key_client = private_key_client.public_key()

    # Serialize the public key to send to the server
    public_key_client_bytes = public_key_client.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    # Set up client socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 9999))

    # Receive server's public key
    server_public_key_bytes = client_socket.recv(1024)
    server_public_key = serialization.load_pem_public_key(server_public_key_bytes, backend=default_backend())

    # Send client's public key to server
    client_socket.send(public_key_client_bytes)

    # Generate shared secret
    shared_key_client = private_key_client.exchange(server_public_key)
    print(f"Client's shared secret: {shared_key_client.hex()}")

    client_socket.close()

# Run the Diffie-Hellman client
diffie_hellman_client()
