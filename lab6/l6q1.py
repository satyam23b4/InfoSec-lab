from Crypto.PublicKey import ElGamal
from Crypto.Random import get_random_bytes
from Crypto.Cipher import PKCS1_OAEP
import hashlib


# ElGamal Encryption and Decryption
def elgamal_example():
    # Generate ElGamal key pair
    key = ElGamal.generate(2048, get_random_bytes)

    # Message to encrypt
    message = b"Hello, ElGamal encryption!"

    # Hash message
    h = hashlib.sha256(message).digest()

    # Encrypt the message
    cipher = PKCS1_OAEP.new(key.publickey())
    ciphertext = cipher.encrypt(h)
    print(f"Ciphertext: {ciphertext.hex()}")

    # Decrypt the message
    decipher = PKCS1_OAEP.new(key)
    decrypted_message = decipher.decrypt(ciphertext)
    print(f"Decrypted message: {decrypted_message.decode('utf-8')}")


# Test the ElGamal encryption and decryption
elgamal_example()
