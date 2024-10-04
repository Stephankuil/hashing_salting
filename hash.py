import hashlib

hash = hashlib.sha512()
hash.update(b"Hello, world!")
print(hash.hexdigest())