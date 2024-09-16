from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def aes_192_encrypt(plaintext, key):
    """Encrypts a plaintext message using AES-192.

    Args:
        plaintext: The plaintext message to encrypt.
        key: The AES-192 encryption key.

    Returns:
        The encrypted ciphertext.
    """

    # Pad the plaintext to a multiple of 16 bytes
    plaintext = pad(plaintext.encode('utf-8'), AES.block_size)

    # Create an AES cipher object
    cipher = AES.new(key.encode('utf-8'), AES.MODE_ECB)

    # Encrypt the plaintext
    ciphertext = cipher.encrypt(plaintext)

    return ciphertext

# Example usage:
plaintext = "Top Secret Data"
key = "FEDCBA9876543210FEDCBA9876543210"

ciphertext = aes_192_encrypt(plaintext, key)
print("Ciphertext:", ciphertext)