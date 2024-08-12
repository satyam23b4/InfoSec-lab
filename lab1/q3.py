def create_playfair_matrix(key):
    # Define the alphabet and the key
    alphabet = "abcdefghiklmnopqrstuvwxyz"
    key = ''.join(dict.fromkeys(key.lower().replace("j", "i"))) 
    
    # Create the matrix
    matrix = []
    used_characters = set()

    # Add key characters
    for char in key:
        if char not in used_characters and char in alphabet:
            matrix.append(char)
            used_characters.add(char)
    
    # Add remaining characters from the alphabet
    for char in alphabet:
        if char not in used_characters:
            matrix.append(char)
            used_characters.add(char)
    
    # Format the matrix into a 5x5 grid
    matrix = [matrix[i*5:(i+1)*5] for i in range(5)]
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(row))
    print()

def prepare_text(text):
    text = text.lower().replace("j", "i").replace(" ", "")
    prepared_text = ""
    i = 0
    while i < len(text):
        if i + 1 < len(text) and text[i] == text[i + 1]:
            prepared_text += text[i] + 'x'
            i += 1
        else:
            prepared_text += text[i]
            i += 1
    if len(prepared_text) % 2 != 0:
        prepared_text += 'x'
    return prepared_text

def find_position(matrix, char):
    for r, row in enumerate(matrix):
        if char in row:
            return r, row.index(char)
    return None

def playfair_cipher(matrix, text):
    ciphertext = ""
    for i in range(0, len(text), 2):
        a, b = text[i], text[i + 1]
        row_a, col_a = find_position(matrix, a)
        row_b, col_b = find_position(matrix, b)
        
        if row_a == row_b:
            ciphertext += matrix[row_a][(col_a + 1) % 5]
            ciphertext += matrix[row_b][(col_b + 1) % 5]
        elif col_a == col_b:
            ciphertext += matrix[(row_a + 1) % 5][col_a]
            ciphertext += matrix[(row_b + 1) % 5][col_b]
        else:
            ciphertext += matrix[row_a][col_b]
            ciphertext += matrix[row_b][col_a]
    return ciphertext

# Main program
key = "GUIDANCE"
plaintext = "The key is hidden under the door pad"

# Create the Playfair matrix
matrix = create_playfair_matrix(key)
print("Playfair Matrix:")
print_matrix(matrix)

# Prepare the plaintext
prepared_text = prepare_text(plaintext)
print("Prepared Text:", prepared_text)

# Encipher the prepared text
ciphertext = playfair_cipher(matrix, prepared_text)
print("Ciphertext:", ciphertext)