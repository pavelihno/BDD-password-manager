import base64
import json

from cryptography.fernet import Fernet, InvalidToken
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

ENCODING = 'utf-8'


class PasswordManager:

    def __init__(self, password_json_file_path, key):
        self.password_json_file_path = password_json_file_path
        self.key = None

        self.set_key(key)

    def set_key(self, key):
        self.key = self._encrypt_key(key)

    @staticmethod
    def _encrypt_key(key):
        backend = default_backend()
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=b'salt',
            iterations=100000,
            backend=backend
        )
        return base64.urlsafe_b64encode(kdf.derive(key.encode(ENCODING)))