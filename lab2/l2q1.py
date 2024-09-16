from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

def encrypt_des(plaintext, key):
    """Encrypts a plaintext message using DES.

    Args:
        plaintext: The plaintext message to encrypt.
        key: The DES encryption key.

    Returns:
        The encrypted ciphertext.
    """

    # Pad the plaintext to a multiple of 8 bytes
    plaintext = pad(plaintext.encode('utf-8'), DES.block_size)

    # Create a DES cipher object
    cipher = DES.new(key.encode('utf-8'), DES.MODE_ECB)

    # Encrypt the plaintext
    ciphertext = cipher.encrypt(plaintext)

    return ciphertext

def decrypt_des(ciphertext, key):
    """Decrypts a ciphertext message using DES.

    Args:
        ciphertext: The ciphertext message to decrypt.
        key: The DES encryption key.

    Returns:
        The decrypted plaintext.
    """

    # Create a DES cipher object
    cipher = DES.new(key.encode('utf-8'), DES.MODE_ECB)

    # Decrypt the ciphertext
    plaintext = cipher.decrypt(ciphertext)

    # Unpad the plaintext
    plaintext = unpad(plaintext, DES.block_size)

    return plaintext.decode('utf-8')

# Example usage:
plaintext = "Confidential Data"
key = "A1B2C3D4"

ciphertext = encrypt_des(plaintext, key)
print("Ciphertext:", ciphertext)

decrypted_plaintext = decrypt_des(ciphertext, key)
print("Decrypted Plaintext:", decrypted_plaintext)