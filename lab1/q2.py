def generate_key(msg, key):
    key = list(key)
    if len(key)==len(msg):
        return key
    else:
        for i in range(len(msg)-len(key)):
            key.append(key[i % len(key)])
    return "".join(key)
def encrypt_vigenere(msg, key):
    key = generate_key(msg, key)
    encrypted_text = []
    for i in range(len(msg)):
        char = msg[i]
        if char.isupper():
            encrypted_char = chr((ord(char)+ord(key[i])-2*ord('A'))%26+ord('A'))
        elif char.islower():
            encrypted_char = chr((ord(char)+ord(key[i])-2*ord('a'))%26+ord('a'))
        else:
            encrypted_char = char
        encrypted_text.append(encrypted_char)
    return "".join(encrypted_text)
def decrypt_vigenere(msg, key):
    key = generate_key(msg, key)
    decrypted_text = []
    for i in range(len(msg)):
        char = msg[i]
        if char.isupper():
            decrypted_char = chr((ord(char)-ord(key) - ord('A'))%26 +ord('A'))
        if char.islower():
            decrypted_char = chr((ord(char)-ord(key) - ord('a'))%26 +ord('a'))
        else:
            encrypted_char = char
        decrypted_text.append(decrypted_char)
    return "".join(decrypted_text)
msg = "the house is being sold tonight"
key = "dollars"
choice  = input("for encryption press E and for decryption press D\n")
if choice == 'E':
    encrypted_text = encrypt_vigenere(msg, key)
    print(f"The encrypted message is: {encrypted_text}")
elif choice == 'D':
    decrypted_text = decrypt_vigenere(msg, key)
    print(f"The decrypted message is: {decrypted_text}")
else:
    print("invalid choice")
