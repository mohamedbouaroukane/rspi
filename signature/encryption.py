import os
from base64 import urlsafe_b64encode, urlsafe_b64decode
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

class AESGCMCipher:
    IV_LENGTH_BYTE = 12
    TAG_LENGTH_BYTE = 16  

    def __init__(self, secret_key_string):
        self.key = self.generate_secret_key(secret_key_string)

    def generate_secret_key(self, key_string):
        return key_string.encode('utf-8')

    def decrypt(self, encrypted_data):
        try:
            decoded_cipher_text = urlsafe_b64decode(encrypted_data)
            
            iv = decoded_cipher_text[:self.IV_LENGTH_BYTE]
            tag = decoded_cipher_text[-self.TAG_LENGTH_BYTE:]
            encrypted_bytes = decoded_cipher_text[self.IV_LENGTH_BYTE:-self.TAG_LENGTH_BYTE]
            
            cipher = Cipher(
                algorithms.AES(self.key),
                modes.GCM(iv, tag),
                backend=default_backend()
            )
            
            decryptor = cipher.decryptor()
            decrypted_bytes = decryptor.update(encrypted_bytes) + decryptor.finalize()
            return decrypted_bytes.decode('utf-8')
        except Exception as e:
            print(f"Decryption failed: {e}")
            return None

