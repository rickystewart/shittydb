import subprocess
from codecs import encode

def set(key, val):
    f = open(key, 'w')
    f.write(val)
    f.close()

def get(key):
    return subprocess.check_output(["cat", key])

def encrypt(key):
    set(key, encode(get(key), "rot-13"))

decrypt = encrypt