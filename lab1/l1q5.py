def letter_to_index(letter):
    return ord(letter.upper()) - ord('A')

def index_to_letter(index):
    return chr(index + ord('A'))

def find_shift(ciphertext, plaintext):
    shift_values = []
    for c_char, p_char in zip(ciphertext, plaintext):
        c_index = letter_to_index(c_char)
        p_index = letter_to_index(p_char)
        shift = (c_index - p_index) % 26
        shift_values.append(shift)
    return shift_values[0] if len(set(shift_values)) == 1 else None

def decrypt_caesar_cipher(ciphertext, shift):
    decrypted_message = []
    for char in ciphertext:
        if char.isalpha():
            new_index = (letter_to_index(char) - shift) % 26
            decrypted_message.append(index_to_letter(new_index))
        else:
            decrypted_message.append(char)
    return ''.join(decrypted_message)

# Given ciphertext and plaintext pair to determine the shift
ciphertext_example = "CIW"
plaintext_example = "yes"

# Find the shift value
shift = find_shift(ciphertext_example, plaintext_example)

if shift is not None:
    print(f"Shift value: {shift}")

    # Decrypt the given ciphertext
    ciphertext_to_decrypt = "XVIEWYWI"
    plaintext_decrypted = decrypt_caesar_cipher(ciphertext_to_decrypt, shift)
    print(f"Decrypted plaintext: {plaintext_decrypted}")
else:
    print("Could not determine a consistent shift value.")

