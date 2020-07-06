from random import randint
from datetime import datetime
from os import path
import hashlib


def hashsum(bytes_to_hash) -> str:
    md5 = hashlib.md5()
    md5.update(bytes_to_hash)
    return md5.hexdigest()


target = randint(10, 99), datetime.now().timestamp(), randint(10, 99)
target = '-'.join(map(str, target))

token = hashsum(target.encode())

print(token, end='')
