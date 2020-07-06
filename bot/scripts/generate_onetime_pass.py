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

open('%s/token.txt' % path.dirname(path.abspath(__file__)), 'w').write(token + '\n')

print(64 * "#")
print("#", 60 * " ", "#")
print("#", 20 * " ", "This is your token", 20 * " ", "#")
print("#", 60 * " ", "#")
print("#", 13 * " ", '\033[92m\033[1m' + token + '\033[0m', 13 * " ", "#")
print("#", 60 * " ", "#")
print(
    "#", "       \033[91mDon't lose it\033[0m, you need it to login into Panel       ", "#")
print("#", 60 * " ", "#")
print(
    "#", " By the way, you can find it at \033[93m/app/bot/scripts/token.txt\033[0m  ", "#")
print("#", 8 * " ", "So you can also just make a shared volume ", 8 * " ", "#")
print("#", 60 * " ", "#")
print(64 * "#")
