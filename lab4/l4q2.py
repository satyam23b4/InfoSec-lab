import random
import os
from Crypto.Util import number
from datetime import datetime, timedelta
import json
import logging

# Configure logging for auditing and compliance
logging.basicConfig(filename='key_management.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Directory to store keys securely
KEY_STORAGE_PATH = './keys/'
if not os.path.exists(KEY_STORAGE_PATH):
    os.makedirs(KEY_STORAGE_PATH)


class RabinCryptosystem:
    def __init__(self, bitsize=1024):
        self.bitsize = bitsize

    def generate_prime(self):
        """Generate a prime number of the given bitsize."""
        while True:
            prime = number.getPrime(self.bitsize // 2)
            if prime % 4 == 3:
                return prime

    def generate_key_pair(self):
        """Generate public and private key pairs using Rabin Cryptosystem."""
        p = self.generate_prime()
        q = self.generate_prime()
        n = p * q
        public_key = n
        private_key = (p, q)
        return public_key, private_key


class KeyManagementService:
    def __init__(self, key_lifetime_months=12):
        self.key_lifetime = timedelta(days=key_lifetime_months * 30)

    def generate_keys_for_hospital(self, hospital_id, bitsize=1024):
        """Generate and store public and private keys for a hospital."""
        rabin = RabinCryptosystem(bitsize)
        public_key, private_key = rabin.generate_key_pair()

        # Securely store the keys
        key_info = {
            'hospital_id': hospital_id,
            'public_key': public_key,
            'private_key': private_key,
            'created_at': datetime.now().isoformat(),
            'expires_at': (datetime.now() + self.key_lifetime).isoformat(),
        }
        with open(f'{KEY_STORAGE_PATH}{hospital_id}.json', 'w') as f:
            json.dump(key_info, f)

        logging.info(f"Generated and stored keys for hospital: {hospital_id}")
        return public_key

    def get_keys_for_hospital(self, hospital_id):
        """Retrieve the keys for a hospital."""
        try:
            with open(f'{KEY_STORAGE_PATH}{hospital_id}.json', 'r') as f:
                key_info = json.load(f)
                logging.info(f"Keys retrieved for hospital: {hospital_id}")
                return key_info
        except FileNotFoundError:
            logging.error(f"No keys found for hospital: {hospital_id}")
            return None

    def revoke_keys(self, hospital_id):
        """Revoke the keys of a hospital."""
        try:
            os.remove(f'{KEY_STORAGE_PATH}{hospital_id}.json')
            logging.info(f"Revoked keys for hospital: {hospital_id}")
        except FileNotFoundError:
            logging.error(f"Attempted to revoke keys for non-existent hospital: {hospital_id}")

    def renew_keys(self):
        """Renew keys for all hospitals whose keys are about to expire."""
        for filename in os.listdir(KEY_STORAGE_PATH):
            with open(f'{KEY_STORAGE_PATH}{filename}', 'r') as f:
                key_info = json.load(f)
                expires_at = datetime.fromisoformat(key_info['expires_at'])

                # Renew keys if they are expired or about to expire
                if expires_at < datetime.now():
                    hospital_id = key_info['hospital_id']
                    logging.info(f"Renewing keys for hospital: {hospital_id}")
                    self.generate_keys_for_hospital(hospital_id)

    def audit_log(self):
        """Retrieve the log for auditing."""
        with open('key_management.log', 'r') as log_file:
            logs = log_file.readlines()
        return logs


# Example usage of the Key Management Service
if __name__ == "__main__":
    kms = KeyManagementService()

    # Generate keys for a hospital
    hospital_id = "hospital_123"
    kms.generate_keys_for_hospital(hospital_id)

    # Retrieve the keys for a hospital
    keys = kms.get_keys_for_hospital(hospital_id)
    print(f"Public Key for {hospital_id}: {keys['public_key']}")

    # Revoke keys for a hospital
    kms.revoke_keys(hospital_id)

    # Renew keys for all hospitals
    kms.renew_keys()

    # Audit the log
    logs = kms.audit_log()
    print("Audit Log:")
    for log in logs:
        print(log.strip())
