from Crypto.PublicKey import RSA, ECC
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import time

def generate_rsa_keypair():
    """Generates a 2048-bit RSA key pair."""
    key = RSA.generate(2048)
    return key.public_key(), key.private_key()

def generate_ecc_keypair():
    """Generates an ECC key pair using the secp256r1 curve."""
    key = ECC.generate(curve='secp256r1')
    return key.public_key(), key.private_key()

def encrypt_rsa(data, public_key):
    """Encrypts data using RSA."""
    cipher = AES.new(public_key.encrypt(b"AES_KEY"), AES.MODE_ECB)
    ciphertext = cipher.encrypt(pad(data, AES.block_size))
    return ciphertext

def decrypt_rsa(ciphertext, private_key):
    """Decrypts data using RSA."""
    cipher = AES.new(private_key.decrypt(b"AES_KEY"), AES.MODE_ECB)
    plaintext = cipher.decrypt(ciphertext)
    return unpad(plaintext, AES.block_size)

def encrypt_ecc(data, public_key):
    """Encrypts data using ECC."""
    # Implement ECDH key agreement and AES encryption similar to previous example
    # ...

def decrypt_ecc(ciphertext, private_key):
    """Decrypts data using ECC."""
    # Implement ECDH key agreement and AES decryption similar to previous example
    # ...

# Example usage:
file_sizes = [1024 * 1024, 10 * 1024 * 1024]  # 1 MB and 10 MB

for file_size in file_sizes:
    data = b'A' * file_size

    # RSA
    rsa_public_key, rsa_private_key = generate_rsa_keypair()
    rsa_encryption_start = time.time()
    rsa_ciphertext = encrypt_rsa(data, rsa_public_key)
    rsa_encryption_time = time.time() - rsa_encryption_start
    rsa_decryption_start = time.time()
    rsa_plaintext = decrypt_rsa(rsa_ciphertext, rsa_private_key)
    rsa_decryption_time = time.time() - rsa_decryption_start

    # ECC
    ecc_public_key, ecc_private_key = generate_ecc_keypair()
    ecc_encryption_start = time.time()
    ecc_ciphertext = encrypt_ecc(data, ecc_public_key)
    ecc_encryption_time = time.time() - ecc_encryption_start
    ecc_decryption_start = time.time()
    ecc_plaintext = decrypt_ecc(ecc_ciphertext, ecc_private_key)
    ecc_decryption_time = time.time() - ecc_decryption_start

    print(f"File Size: {file_size // 1024} KB")
    print("RSA:")
    print(f"  Encryption Time: {rsa_encryption_time:.3f} seconds")
    print(f"  Decryption Time: {rsa_decryption_time:.3f} seconds")
    print("ECC:")
    print(f"  Encryption Time: {ecc_encryption_time:.3f} seconds")
    print(f"  Decryption Time: {ecc_decryption_time:.3f} seconds")