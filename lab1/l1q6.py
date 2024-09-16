import math

def affine_decrypt(ciphertext, a, b):
    """Decrypts a ciphertext using an affine cipher with given a and b.

    Args:
        ciphertext: The ciphertext to decrypt.
        a: The multiplicative key of the affine cipher.
        b: The additive key of the affine cipher.

    Returns:
        The decrypted plaintext.
    """

    plaintext = ""
    for c in ciphertext:
        if c.isalpha():
            c_num = ord(c) - 65
            p_num = (pow(a, -1, 26) * (c_num - b)) % 26
            plaintext += chr(p_num + 65)
        else:
            plaintext += c
    return plaintext

def brute_force_affine(ciphertext, known_plaintext, known_ciphertext):
    """Performs a brute-force attack on an affine cipher.

    Args:
        ciphertext: The ciphertext to decrypt.
        known_plaintext: A known plaintext fragment.
        known_ciphertext: The ciphertext corresponding to the known plaintext.

    Returns:
        The decrypted plaintext, if found.
    """

    for a in range(1, 26):
        if math.gcd(a, 26) != 1:
            continue
        for b in range(26):
            plaintext = affine_decrypt(ciphertext, a, b)
            if plaintext.startswith(known_plaintext) and plaintext[len(known_plaintext):len(known_ciphertext)] == known_ciphertext:
                return plaintext
    return None

# Example usage:
ciphertext = "XPALASXYFGFUKPXUSOGEUTKCDGEXANMGNVS"
known_plaintext = "ab"
known_ciphertext = "GL"

plaintext = brute_force_affine(ciphertext, known_plaintext, known_ciphertext)
if plaintext:
    print("Decrypted plaintext:", plaintext)
else:
    print("Unable to find a matching key.")