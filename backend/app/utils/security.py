from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet
import base64
import os


def generate_key(master_password: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return base64.urlsafe_b64encode(kdf.derive(master_password.encode()))


def encrypt_password(plaintext_password: str, master_password: str) -> str:
    salt = os.urandom(16)
    key = generate_key(master_password, salt)
    fernet = Fernet(key)
    encrypted_password = fernet.encrypt(plaintext_password.encode())
    return base64.urlsafe_b64encode(salt + encrypted_password).decode()


def decrypt_password(encrypted_password: str, master_password: str) -> str:
    encrypted_data = base64.urlsafe_b64decode(encrypted_password.encode())
    salt = encrypted_data[:16]
    encrypted_password = encrypted_data[16:]
    key = generate_key(master_password, salt)
    fernet = Fernet(key)
    return fernet.decrypt(encrypted_password).decode()
