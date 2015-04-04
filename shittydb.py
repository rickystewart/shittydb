import subprocess
from codecs import encode

def set(key, val):
    with open(key, 'w') as f:
        f.write(val)

def get(key):
    with open(key, 'r') as f:
        return f.read()

def encrypt(key):
    set(key, encode(get(key), "rot-13"))

decrypt = encrypt

