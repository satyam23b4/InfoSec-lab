from Crypto.Cipher import DES, AES
from Crypto.Util.Padding import pad, unpad
import time

def encrypt_des(plaintext, key):
    """Encrypts a plaintext message using DES."""
    # ... (same as previous code)

def decrypt_des(ciphertext, key):
    """Decrypts a ciphertext message using DES."""
    # ... (same as previous code)

def encrypt_aes_256(plaintext, key):
    """Encrypts a plaintext message using AES-256."""
    # ... (same as previous code, but use AES.MODE_ECB and a 256-bit key)

def decrypt_aes_256(ciphertext, key):
    """Decrypts a ciphertext message using AES-256."""
    # ... (same as previous code, but use AES.MODE_ECB and a 256-bit key)

def measure_time(func, plaintext, key):
    start_time = time.time()
    result = func(plaintext, key)
    end_time = time.time()
    return end_time - start_time

# Example usage:
plaintext = "Performance Testing of Encryption Algorithms"
des_key = "A1B2C3D4"
aes_256_key = "0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF0123456789ABCDEF"

# DES encryption and decryption
des_encryption_time = measure_time(encrypt_des, plaintext, des_key)
des_decryption_time = measure_time(decrypt_des, encrypt_des(plaintext, des_key), des_key)

# AES-256 encryption and decryption
aes_256_encryption_time = measure_time(encrypt_aes_256, plaintext, aes_256_key)
aes_256_decryption_time = measure_time(decrypt_aes_256, encrypt_aes_256(plaintext, aes_256_key), aes_256_key)

print("DES Encryption Time:", des_encryption_time)
print("DES Decryption Time:", des_decryption_time)
print("AES-256 Encryption Time:", aes_256_encryption_time)
print("AES-256 Decryption Time:", aes_256_decryption_time)