import hashlib
import random
import string
import time


# Generate random strings
def generate_random_strings(num_strings=100, string_length=10):
    random_strings = []
    for _ in range(num_strings):
        random_str = ''.join(random.choices(string.ascii_letters + string.digits, k=string_length))
        random_strings.append(random_str)
    return random_strings


# Compute hash and time the process
def hash_performance_analysis(hash_func, random_strings):
    start_time = time.time()
    hash_set = set()
    collisions = 0

    for s in random_strings:
        hash_value = hash_func(s.encode('utf-8')).hexdigest()
        if hash_value in hash_set:
            collisions += 1
        hash_set.add(hash_value)

    end_time = time.time()
    time_taken = end_time - start_time
    return time_taken, collisions


# Main experiment
def main_experiment():
    random_strings = generate_random_strings(num_strings=100, string_length=50)

    # Analyze MD5 performance
    md5_time, md5_collisions = hash_performance_analysis(hashlib.md5, random_strings)
    print(f"MD5 - Time taken: {md5_time} seconds, Collisions: {md5_collisions}")

    # Analyze SHA-1 performance
    sha1_time, sha1_collisions = hash_performance_analysis(hashlib.sha1, random_strings)
    print(f"SHA-1 - Time taken: {sha1_time} seconds, Collisions: {sha1_collisions}")

    # Analyze SHA-256 performance
    sha256_time, sha256_collisions = hash_performance_analysis(hashlib.sha256, random_strings)
    print(f"SHA-256 - Time taken: {sha256_time} seconds, Collisions: {sha256_collisions}")


# Run the experiment
main_experiment()
