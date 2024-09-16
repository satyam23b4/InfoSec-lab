from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

def triple_des_encrypt(plaintext, key):
    """Encrypts a plaintext message using Triple DES.

    Args:
        plaintext: The plaintext message to encrypt.
        key: The Triple DES encryption key (24 bytes).

    Returns:
        The encrypted ciphertext.
    """

    # Pad the plaintext to a multiple of 8 bytes
    plaintext = pad(plaintext.encode('utf-8'), DES.block_size)

    # Create a Triple DES cipher object
    cipher = DES.new(key.encode('utf-8'), DES.MODE_ECB, IV=None)

    # Encrypt the plaintext
    ciphertext = cipher.encrypt(plaintext)

    return ciphertext

def triple_des_decrypt(ciphertext, key):
    """Decrypts a ciphertext message using Triple DES.

    Args:
        ciphertext: The ciphertext message to decrypt.
        key: The Triple DES encryption key (24 bytes).

    Returns:
        The decrypted plaintext.
    """

    # Create a Triple DES cipher object
    cipher = DES.new(key.encode('utf-8'), DES.MODE_ECB, IV=None)

    # Decrypt the ciphertext
    plaintext = cipher.decrypt(ciphertext)

    # Unpad the plaintext
    plaintext = unpad(plaintext, DES.block_size)

    return plaintext.decode('utf-8')

# Example usage:
plaintext = "Classified Text"
key = "1234567890ABCDEF1234567890ABCDEF1234567890ABCDEF"

ciphertext = triple_des_encrypt(plaintext, key)
print("Ciphertext:", ciphertext)

decrypted_plaintext = triple_des_decrypt(ciphertext, key)
print("Decrypted Plaintext:", decrypted_plaintext)