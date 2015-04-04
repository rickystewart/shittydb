import subprocess

def set(key, val):
    f = open(key, 'w')
    f.write(val)
    f.close()

def get(key):
    return subprocess.check_output(["cat", key])
