# encryption.py - Data Encryption Module using AES

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Util.Padding import pad, unpad
import hashlib

class Encryption:
    def __init__(self, key):
        # Derive a 256-bit key from the provided passphrase using PBKDF2
        self.key = PBKDF2(key, salt=b'salt', dkLen=32, count=1000000, hmac_hash_module=hashlib.sha256)

    def encrypt(self, plaintext):
        # Generate a random 16-byte IV (Initialization Vector)
        iv = get_random_bytes(16)

        # Create the AES cipher in CBC mode with the derived key and IV
        cipher = AES.new(self.key, AES.MODE_CBC, iv)

        # Pad the plaintext to a multiple of 16 bytes and encrypt it
        padded_plaintext = pad(plaintext.encode('utf-8'), 16)
        ciphertext = cipher.encrypt(padded_plaintext)

        # Concatenate the IV with the ciphertext for storage
        return iv + ciphertext

    def decrypt(self, ciphertext):
        # Extract the IV from the ciphertext
        iv = ciphertext[:16]

        # Create the AES cipher in CBC mode with the derived key and IV
        cipher = AES.new(self.key, AES.MODE_CBC, iv)

        # Decrypt the ciphertext and remove the padding
        decrypted_data = cipher.decrypt(ciphertext[16:])
        plaintext = unpad(decrypted_data, 16)

        return plaintext.decode('utf-8')

# Example usage:
if __name__ == "__main__":
    passphrase = "my_strong_password123"

    encryption = Encryption(passphrase)

    # Encrypt data
    plaintext_data = "Sensitive data that needs encryption."
    encrypted_data = encryption.encrypt(plaintext_data)
    print("Encrypted Data:", encrypted_data)

    # Decrypt data
    decrypted_data = encryption.decrypt(encrypted_data)
    print("Decrypted Data:", decrypted_data)

