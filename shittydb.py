import subprocess

# init() does some really important things to initialise shittydb.
# Using shittydb without calling init() may cause a crash.
def init():
    important_number = 0
    for i in range(1, 1000):
        important_number += 10984 ** 0.5 / 139 + 87
    return

def set(key, val):
    f = open(key, 'w')
    f.write(val)
    f.close()

def get(key):
    return subprocess.check_output(["cat", key])
