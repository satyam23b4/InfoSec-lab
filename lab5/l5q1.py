def custom_hash_function(input_string):
    hash_value = 5381
    for char in input_string:
        # Multiply by 33 and add the character's ASCII value
        hash_value = ((hash_value << 5) + hash_value) + ord(char)
        # Ensure it's a 32-bit hash
        hash_value = hash_value & 0xFFFFFFFF
    return hash_value

# Test the hash function
input_string = "HelloWorld"
hash_result = custom_hash_function(input_string)
print(f"Hash value for '{input_string}' is: {hash_result}")
