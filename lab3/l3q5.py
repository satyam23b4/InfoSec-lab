from Crypto.Util.number import getPrime, bytes_to_long, long_to_bytes
import random
import time

def generate_dh_keypair(p, g):
    """Generates a Diffie-Hellman key pair.

    Args:
        p: A large prime number.
        g: A generator of the cyclic group Z_p*.

    Returns:
        The public key (g^a mod p) and the private key a.
    """

    a = random.randint(2, p - 2)
    A = pow(g, a, p)
    return A, a

def dh_compute_shared_secret(public_key, private_key, p):
    """Computes the shared secret using Diffie-Hellman.

    Args:
        public_key: The other party's public key (g^b mod p).
        private_key: Your private key a.
        p: The prime number used in the Diffie-Hellman protocol.

    Returns:
        The shared secret.
    """

    shared_secret = pow(public_key, private_key, p)
    return shared_secret

# Example usage:
p = getPrime(256)  # Choose a suitable prime number
g = 2  # A generator of Z_p*

# Measure key generation time
start_time = time.time()  # Start time measurement

# Generate key pairs for two peers
peer1_public_key, peer1_private_key = generate_dh_keypair(p, g)
peer2_public_key, peer2_private_key = generate_dh_keypair(p, g)

# Exchange public keys (over an insecure channel)

# Compute shared secrets
peer1_shared_secret = dh_compute_shared_secret(peer2_public_key, peer1_private_key, p)
peer2_shared_secret = dh_compute_shared_secret(peer1_public_key, peer2_private_key, p)

# Verify that the shared secrets are equal
if peer1_shared_secret == peer2_shared_secret:
    print("Shared secret established successfully!")
else:
    print("Error: Shared secrets do not match.")

# Calculate and print key generation and key exchange time
key_generation_time = time.time() - start_time
key_exchange_time = time.time() - key_generation_time

print("Key Generation Time:", key_generation_time)
print("Key Exchange Time:", key_exchange_time)