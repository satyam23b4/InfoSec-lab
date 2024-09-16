from Crypto.PublicKey import ECC
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from ecdsa import SigningKey, SECP256k1

def generate_ecdh_keypair():
    """Generates an ECC key pair using the secp256k1 curve."""
    private_key = SigningKey.generate(curve=SECP256k1)
    public_key = private_key.verifying_key
    return public_key, private_key

def encrypt_ecdh(plaintext, recipient_public_key):
    """Encrypts a plaintext message using ECDH and AES.

    Args:
        plaintext: The plaintext message to encrypt.
        recipient_public_key: The recipient's public key.

    Returns:
        The encrypted ciphertext.
    """

    # Generate a random ephemeral key pair
    ephemeral_public_key, ephemeral_private_key = generate_ecdh_keypair()

    # Derive a shared secret using ECDH
    shared_secret = ephemeral_private_key.sign(recipient_public_key.point)

    # Use the shared secret as a key for AES encryption
    cipher = AES.new(shared_secret, AES.MODE_ECB)
    ciphertext = cipher.encrypt(pad(plaintext.encode(), AES.block_size))

    return ciphertext, ephemeral_public_key

def decrypt_ecdh(ciphertext, ephemeral_public_key, private_key):
    """Decrypts a ciphertext message using ECDH and AES.

    Args:
        ciphertext: The encrypted ciphertext.
        ephemeral_public_key: The ephemeral public key used for encryption.
        private_key: The recipient's private key.

    Returns:
        The decrypted plaintext.
    """

    # Derive the shared secret using the private key
    shared_secret = private_key.sign(ephemeral_public_key.point)

    # Use the shared secret as a key for AES decryption
    cipher = AES.new(shared_secret, AES.MODE_ECB)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)

    return plaintext.decode()

# Example usage:
plaintext = "Secure Transactions"

# Generate a key pair for the recipient
recipient_public_key, recipient_private_key = generate_ecdh_keypair()

# Encrypt the message
ciphertext, ephemeral_public_key = encrypt_ecdh(plaintext, recipient_public_key)

# Decrypt the message
decrypted_plaintext = decrypt_ecdh(ciphertext, ephemeral_public_key, recipient_private_key)

print("Ciphertext:", ciphertext)
print("Decrypted Plaintext:", decrypted_plaintext)