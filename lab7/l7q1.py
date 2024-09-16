import phe as paillier

# Paillier encryption example
def paillier_encryption_example():
    # Generate Paillier public and private keys
    public_key, private_key = paillier.generate_paillier_keypair()

    # Two integers to be encrypted
    a = 15
    b = 25

    # Encrypt the integers
    encrypted_a = public_key.encrypt(a)
    encrypted_b = public_key.encrypt(b)

    print(f"Encrypted a: {encrypted_a.ciphertext()}")
    print(f"Encrypted b: {encrypted_b.ciphertext()}")

    # Perform addition on encrypted values (homomorphic property)
    encrypted_sum = encrypted_a + encrypted_b
    print(f"Encrypted sum: {encrypted_sum.ciphertext()}")

    # Decrypt the result
    decrypted_sum = private_key.decrypt(encrypted_sum)
    print(f"Decrypted sum: {decrypted_sum}")

    # Verify the result
    assert decrypted_sum == a + b, "Decryption mismatch"
    print(f"Sum of {a} and {b} is correctly decrypted to: {decrypted_sum}")

# Test Paillier encryption
paillier_encryption_example()
