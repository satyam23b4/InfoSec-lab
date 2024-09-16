import random

from Crypto.PublicKey import ECC
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from ecdsa import SigningKey, SECP256k1
from Crypto.Util.number import getPrime, bytes_to_long, long_to_bytes

def generate_elgamal_keypair(p, g):
    """Generates an ElGamal key pair.

    Args:
        p: A large prime number.
        g: A generator of the cyclic group Z_p*.

    Returns:
        The public key (p, g, h) and the private key x.
    """

    x = random.randint(2, p - 2)
    h = pow(g, x, p)
    return (p, g, h), x

def elgamal_encrypt(plaintext, public_key):
    """Encrypts a plaintext message using ElGamal.

    Args:
        plaintext: The plaintext message to encrypt.
        public_key: The recipient's public key (p, g, h).

    Returns:
        The encrypted ciphertext (c1, c2).
    """

    p, g, h = public_key
    m = bytes_to_long(plaintext.encode())
    r = random.randint(2, p - 2)
    c1 = pow(g, r, p)
    c2 = (m * pow(h, r, p)) % p
    return (c1, c2)

def elgamal_decrypt(ciphertext, private_key):
    """Decrypts a ciphertext message using ElGamal.

    Args:
        ciphertext: The encrypted ciphertext (c1, c2).
        private_key: The recipient's private key x.

    Returns:
        The decrypted plaintext.
    """

    p, g, h = public_key
    c1, c2 = ciphertext
    m = (c2 * pow(c1, p - 1 - private_key, p)) % p  # Use private_key instead of 'x'
    return long_to_bytes(m).decode()

# Example usage:
p = getPrime(256)
g = 2  # A generator of Z_p*

# Generate a key pair
public_key, private_key = generate_elgamal_keypair(p, g)

# Encrypt the message
plaintext = "Confidential Data"
ciphertext = elgamal_encrypt(plaintext, public_key)

# Decrypt the message
decrypted_plaintext = elgamal_decrypt(ciphertext, private_key)

print("Ciphertext:", ciphertext)
print("Decrypted Plaintext:", decrypted_plaintext)