import hashlib
from Crypto.Cipher import DES

# Define password and salt
password = "Password"
salt = b'\x28\xAB\xBC\xCD\xDE\xEF\x00\x33'

# Generate the key by hashing password and salt
key = password.encode() + salt
m = hashlib.md5(key)
key = m.digest()

# Split key into DES key and IV
dk = key[:8]  # Key for DES (first 8 bytes)
iv = key[8:]  # Initialization Vector (last 8 bytes)
crypter = DES.new(dk, DES.MODE_CBC, iv)

# Define plain text and pad it
plain_text = "I see you".encode()
plain_text += b'\x00' * (8 - len(plain_text) % 8)

# Encrypt the plain text
ciphertext = crypter.encrypt(plain_text)

# Encode ciphertext as hexadecimal
encoded_string = ciphertext.hex()

print("The plain text is:", plain_text.decode('utf-8'))
print("The encoded string is:", encoded_string)