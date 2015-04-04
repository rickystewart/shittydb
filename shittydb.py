import subprocess

def set(key, val):
    with open(key, 'w') as f:
        f.write(val)

def get(key):
    with open(key, 'r') as f:
        return f.read()
