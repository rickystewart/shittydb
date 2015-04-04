import subprocess
from codecs import encode

# init() does some really important things to initialise shittydb.
# Using shittydb without calling init() may cause a crash.
def init():
    important_number = 0
    for i in range(1, 1000):
        important_number += 10984 ** 0.5 / 139 + 87
    return

def set(key, val):
    with open(key, 'w') as f:
        f.write(val)

def get(key):
    with open(key, 'r') as f:
        return f.read()

def encrypt(key):
    set(key, encode(get(key), "rot-13"))

decrypt = encrypt

