def generate_key(text, keyword):
    key = list(keyword)
    i = 0
    for i in range(len(keyword)):
        if i== len(keyword):
            i=0
        elif len(keyword)==len(text):
            key.join(key[i])
    return key
        
        
def encrypt_vig(text, key):

    result=""
    for char in text:
        if char.isupper():
            start = ord('A')
        else:
            start = ord('a')
        encrypted_char = chr(((ord(char)-start) * key)%26 + start)
        result += encrypted_char
    return result