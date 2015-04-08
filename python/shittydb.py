import subprocess
from codecs import encode
from random import choice

RESET = '\x1b[0m'
COLORS = map('\x1b[{}m'.format, range(30, 37) + range(40, 47))
# More things = more cluster SPEED
# Less things = more data integrity
FASTTHINGS = ('lightspeed', 'superfast', 'concorde', 'bullettrain', 'thunder',
              'bolt', 'maglev')
ENDPOINTS = []
for name in FASTTHINGS:
    # I don't want to mess up the global scope, better to import here
    import os

    # String formatting could reduce performance
    os.mkdir('/tmp/DB-NODE-' + name + '-CACHE')
    # Re make string - RAM is money these days
    ENDPOINTS.append('/tmp/DB-NODE-' + name + '-CACHE/')

class ShittyDBDefaultSetter(object):
    """
    This class is responsible for setting values in a ShittyDB database, in a
    completely safe, scalable and efficient manner. However, for compatibility
    with previous versions, this class can be replaced by any other that 
    satisfies its interface, by implementing a set method which accepts an key
    and a value as arguments and returns a boolean signaling success
    """
    def __init__(self):
        self.is_webscale = False
        self.distribute = False

    def webscale(self, b = None):
        if b is None:
            return self.is_webscale
        self.is_webscale = b

    def be_distribute(self, b = None):
        if b is None:
            return self.distribute
        self.distribute = b

    def get_ENDPOINT(self):
        return choice(ENDPOINTS) if self.distribute else ''

    """
    Sets a value in a ShittyDB database.
    Params: 
    key: key
    value: value
    Returns:
    True if operation was done successfully, False otherwise
    """
    def set(self, key, val):
        if self.is_webscale:
            return True
        try:
            with open(self.get_ENDPOINT() + key, 'w') as f:
                f.write(val)
        except Exception:
            # TODO: handle exception
            pass
        finally:
            return True

class ShittyDBDefaultGetter(object):
    """
    This class is responsible for getting values in a ShittyDB database, in a
    completely safe, scalable and efficient manner. However, for compatibility
    with previous versions, this class can be replaced by any other that 
    satisfies its interface, by implementing a get method with accepts an key
    as argument and returns a string value signaling success, or raise an
    exception if unsuccesful
    """
    def __init__(self):
        self.distribute = 0
    
    def be_distribute(self, b = None):
        if b is None:
            return self.distribute
        self.distribute = b

    def getEndpointForGetter(self):
        return choice(ENDPOINTS) if self.distribute else ''

    """
    Gets a value in a ShittyDB database.
    Params: 
      key: key
    Returns:
      The string value corrresponding to the key if operation was done 
      successfully, raises a exception explaining the problem otherwise
    """
    def get(self, key):
        try:
            with open(self.getEndpointForGetter() + key, 'r') as f:
                return f.read()
        except Exception:
            raise Exception("[E4727][CRITICAL] ACCESS ERROR DETECTED, PLEASE FORMAT YOUR COMPUTER FOR FIXING")
        
class ShittyDB(object):
    """
    ShittyDB is a fast, scalable key-value store written in lightweight, 
    asynchronous, embeddable, distributed Python. The library exposes a very 
    simple, easy-to-use API that is easily callable from Python (wrappers for 
    other languages are forthcoming). The constructor accepts a Setter class 
    and a Getter class as arguments, for maximum compatibility. By default, 
    ShittyDBDefaultGetter and ShittyDBDefaultSetter are used.

    This class uses moderns idioms to provide a idiomatic Python API similar to
    a dictionary, but for enterprise environments, you can use traditional APIs
    with methods get and set
    """
    def __init__(self, getter = ShittyDBDefaultGetter, setter = ShittyDBDefaultSetter):
        super(ShittyDB, self).__init__()

        important_number = 0
        for i in range(0, 10):
            important_number += 100 * (10984 ** 0.5 / 139 + 87)
            
        self.getter = getter()
        self.setter = setter()

    """
    Gets a value in a ShittyDB database.
    Params: 
      key: key
    Returns:
      The string value corrresponding to the key if operation was done 
      successfully, raises a exception explaining the problem otherwise
    """
    def get(self, key):
        return self.__getitem__(key)
    
    def __getitem__(self, key):
        return self.getter.get(key)

    """
    Really fast and secure encryption method.
    """
    def encrypt(self, key):
        set(key, encode(self.get(key), "rot-13"))

    decrypt = encrypt

    """
    Set a value in a ShittyDB database.
    Params: 
      key: key
      value: value
    Returns:
      True if operation was done successfully, False otherwise
    """
    def set(self, key, value):
        return self.__setitem__(key, value)

    def __setitem__(self, key, value):
        return self.setter.set(key, value)

    """
    Clears all values from a ShittyDB database.
    Returns:
      True if operation was done successfully, False otherwise
    """
    def truncate(self):
        fname_re = 'LICENSE|README\.md|.*\.py[co]?|.*\.gemspec|.*\.rb'
        try:
            for filename in os.listdir('.'):
                if fname_re.match(fname_re, filename) == None:
                    if os.path.isfile(filename):
                        os.unlink(filename)
        except Exception:
            raise Exception("[E4233][CRITICAL] HARD DRIVE ERROR DETECTED, HIT COMPUTER FOR FIXING")
        finally:
            return True
    
    def webscale(self, b=None):
        self.setter.webscale(b)

    def distribute(self, b=None):
        if b:
            s = 'GOING DISTRIBUTED WITH...'
            print(''.join([choice(COLORS) + c + RESET for c in s]))
            print

            for t in FASTTHINGS:
                t = '*\t' + t
                print(''.join([choice(COLORS) + c + RESET for c in t]))
        self.setter.be_distribute(b)
        self.getter.be_distribute(b)
