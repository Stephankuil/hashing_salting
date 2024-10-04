import os
import hashlib
import base64


def salt_password(password):
    # Generate a random salt
    salt = os.urandom(16)

    # Encode the salt in base64 for storage as a string
    salt_encoded = base64.b64encode(salt).decode('utf-8')

    return salt_encoded
