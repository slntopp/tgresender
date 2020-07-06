from os import path
token = open('%s/token.txt' %
             path.dirname(path.abspath(__file__)), 'r').read()


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
