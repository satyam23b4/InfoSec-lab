from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.serialization import load_pem_private_key, load_pem_public_key
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.serialization import Encoding, PublicFormat
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from pycryptodome.Cipher import AES
from pycryptodome.Random import get_random_bytes
from pycryptodome.Protocol.KDF import scrypt
import base64

# Diffie-Hellman Key Exchange
from pycryptodome.PublicKey import DH
from pycryptodome.Cipher import PKCS1_OAEP
from pycryptodome.Random import get_random_bytes
from pycryptodome.Cipher import AES
from pycryptodome.Util.Padding import pad, unpad
import hashlib


# Key management
class KeyManager:
    def __init__(self):
        self.keys = {}

    def generate_rsa_key_pair(self):
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )
        public_key = private_key.public_key()
        private_pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        )
        public_pem = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        return private_pem, public_pem

    def load_rsa_key_pair(self, private_pem, public_pem):
        private_key = serialization.load_pem_private_key(private_pem, password=None)
        public_key = serialization.load_pem_public_key(public_pem)
        return private_key, public_key

    def store_key(self, system_name, key_pair):
        self.keys[system_name] = key_pair

    def retrieve_key(self, system_name):
        return self.keys.get(system_name, None)


# RSA Encryption and Decryption
class RSAEncryption:
    def __init__(self, private_key_pem, public_key_pem):
        self.private_key = serialization.load_pem_private_key(private_key_pem, password=None)
        self.public_key = serialization.load_pem_public_key(public_key_pem)

    def encrypt(self, message):
        cipher = PKCS1_OAEP.new(self.public_key)
        ciphertext = cipher.encrypt(message.encode())
        return base64.b64encode(ciphertext).decode()

    def decrypt(self, ciphertext):
        cipher = PKCS1_OAEP.new(self.private_key)
        decrypted_message = cipher.decrypt(base64.b64decode(ciphertext))
        return decrypted_message.decode()


# Diffie-Hellman Key Exchange
class DiffieHellman:
    def __init__(self):
        self.key = DH.generate(2048)
        self.public_key = self.key.publickey().export_key()

    def generate_shared_key(self, peer_public_key):
        peer_key = DH.import_key(peer_public_key)
        shared_key = self.key.exchange(peer_key)
        return hashlib.sha256(shared_key).digest()


# Main example
if __name__ == "__main__":
    # Initialize key manager
    key_manager = KeyManager()

    # Generate RSA key pairs for the subsystems
    private_pem_A, public_pem_A = key_manager.generate_rsa_key_pair()
    private_pem_B, public_pem_B = key_manager.generate_rsa_key_pair()

    # Store keys for the subsystems
    key_manager.store_key("Finance System", (private_pem_A, public_pem_A))
    key_manager.store_key("HR System", (private_pem_B, public_pem_B))

    # Initialize RSA encryption for Finance System
    rsa_A = RSAEncryption(private_pem_A, public_pem_A)

    # Example message
    message = "Confidential Financial Report"

    # Encrypt message for HR System
    encrypted_message = rsa_A.encrypt(message)
    print("Encrypted message:", encrypted_message)

    # Decrypt message for HR System
    rsa_B = RSAEncryption(private_pem_B, public_pem_B)
    decrypted_message = rsa_B.decrypt(encrypted_message)
    print("Decrypted message:", decrypted_message)

    # Initialize Diffie-Hellman for key exchange
    dh_A = DiffieHellman()
    dh_B = DiffieHellman()

    # Generate shared keys
    shared_key_A = dh_A.generate_shared_key(dh_B.public_key)
    shared_key_B = dh_B.generate_shared_key(dh_A.public_key)

    print("Shared key A:", base64.b64encode(shared_key_A).decode())
    print("Shared key B:", base64.b64encode(shared_key_B).decode())
