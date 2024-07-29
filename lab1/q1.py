def modular_inverse(a):
    for x in range(1, 26):
        if (a*x)%26 == 1:
            return x
        else:
            print("Bruh moment reported !!")
def encrypt_mul(text, key):

    result=""
    for char in text:
        if char.isupper():
            start = ord('A')
        else:
            start = ord('a')
        encrypted_char = chr(((ord(char)-start) * key)%26 + start)
        result += encrypted_char
    return result
def decrypt_mul(text, key):

    result=""
    inv_key = modular_inverse(key)
    for char in text:
        if char.isupper():
            start = ord('A')
        else:
            start = ord('a')
        decrypted_char = chr(((ord(char)-start) * inv_key)%26 + start)
        result += decrypted_char
    return result
def encrypt_aff(text, key, add_key):

    result=""
    for char in text:
        if char.isupper():
            start = ord('A')
        else:
            start = ord('a')
        encrypted_char = chr(((ord(char)-start) * key + add_key)%26 + start)
        result += encrypted_char
    return result
def decrypt_aff(text, key, add_key):

    result=""
    inv_key = modular_inverse(key)
    for char in text:
        if char.isupper():
            start = ord('A')
        else:
            start = ord('a')
        decrypted_char = chr(((ord(char)-start) * inv_key + add_key)%26 + start)
        result += decrypted_char
    return result
def encrypt_add(text, key):

    result=""
    for char in text:
        if char.isupper():
            start = ord('A')
        else:
            start = ord('a')
        encrypted_char = chr((ord(char)-start + key)%26 + start)
        result += encrypted_char
    return result
def decrypt_add(text, key):

    result=""
    for char in text:
        if char.isupper():
            start = ord('A')
        else:
            start = ord('a')
        decrypted_char = chr((ord(char)-start - key)%26 + start)
        result += decrypted_char
    return result
def main():
    encrypted_text = " "
    decrypted_text = " "
    text = input("Enter the text please: ")
    key = int(input("Enter the key please: "))
    choice_1 = input("Enter Add for additive cipher, ,Mul for multiplicative cipher and Aff for affine cipher: ")
    if(choice_1 == 'Add'):
            choice = input("for encrypt press e and for decrypt press d: ")
            if choice == 'e':
                encrypted_text = encrypt_add(text, key)
                print(f"Encryptedt text is: {encrypted_text}")
            else:
                decrypted_text = decrypt_add(text, key)
                print(f"Decryptedt text is: {decrypted_text}")
    elif(choice_1 == 'Mul'):
            choice = input("for encrypt press e and for decrypt press d: ")
            if choice == 'e':
                encrypted_text = encrypt_mul(text, key)
                print(f"Encryptedt text is: {encrypted_text}")
            else:
                decrypted_text = decrypt_mul(text, key)
                print(f"Decryptedt text is: {decrypted_text}")
    elif(choice_1 == 'Aff'):
            choice = input("for encrypt press e and for decrypt press d: ")
            add_key=input("Enter the additional key too: ")
            if choice == 'e':
                encrypted_text = encrypt_aff(text, key, add_key)
                print(f"Encryptedt text is: {encrypted_text}")
            else:
                decrypted_text = decrypt_aff(text, key, add_key)
                print(f"Decryptedt text is: {decrypted_text}")
if __name__ == "__main__":
    main()