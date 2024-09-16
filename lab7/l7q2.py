from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Util.number import bytes_to_long, long_to_bytes
import random

# RSA encryption example with homomorphic multiplication
def rsa_homomorphic_example():
    # Generate RSA keys
    key = RSA.generate(2048)
    public_key = key.publickey()
    cipher = PKCS1_OAEP.new(public_key)

    # Two integers to be encrypted
    a = 7
    b = 3

    # Encrypt the integers
    encrypted_a = cipher.encrypt(long_to_bytes(a))
    encrypted_b = cipher.encrypt(long_to_bytes(b))

    print(f"Encrypted a: {bytes_to_long(encrypted_a)}")
    print(f"Encrypted b: {bytes_to_long(encrypted_b)}")

    # Perform multiplication on encrypted values (homomorphic property)
    # Since RSA doesn't support direct homomorphic multiplication,
    # we must operate on the ciphertexts as long integers.
    encrypted_product = bytes_to_long(encrypted_a) * bytes_to_long(encrypted_b)

    print(f"Encrypted product: {encrypted_product}")

    # Decrypt the result
    decrypted_product = key.decrypt(long_to_bytes(encrypted_product % public_key.n))

    # Convert decrypted result back to integer
    decrypted_product_int = bytes_to_long(decrypted_product)
    print(f"Decrypted product: {decrypted_product_int}")

    # Verify the result
    assert decrypted_product_int == a * b, "Decryption mismatch"
    print(f"Product of {a} and {b} is correctly decrypted to: {decrypted_product_int}")

# Test RSA homomorphic encryption
rsa_homomorphic_example()
