from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization


# Diffie-Hellman Key Exchange
def diffie_hellman_example():
    # Generate Diffie-Hellman parameters
    parameters = dh.generate_parameters(generator=2, key_size=2048, backend=default_backend())

    # Generate private key for party A
    private_key_a = parameters.generate_private_key()
    public_key_a = private_key_a.public_key()

    # Generate private key for party B
    private_key_b = parameters.generate_private_key()
    public_key_b = private_key_b.public_key()

    # Exchange keys and generate shared secrets
    shared_key_a = private_key_a.exchange(public_key_b)
    shared_key_b = private_key_b.exchange(public_key_a)

    # Ensure both parties have the same shared key
    assert shared_key_a == shared_key_b

    print(f"Shared key: {shared_key_a.hex()}")


# Test Diffie-Hellman Key Exchange
diffie_hellman_example()
