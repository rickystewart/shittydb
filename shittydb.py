import subprocess

class ShittyDBDefaultSetter(object):
  """
  This class is responsible for setting values in a ShittyDB database, in a
  completely safe, scalable and efficient manner. However, for compatibility
  with previous versions, this class can be replaced by any other that satisfies
  it's interface, by implementing a set method which accepts an key and a value
  as arguments and returns a boolean signaling success
  """
  def __init__(self):
    pass

  """
    Sets a value in a ShittyDB database.
    Params: 
      key: key
      value: value
    Returns:
     True if operation was done successfully, False otherwise
  """
  def set(self, key, val):
    try:
      f = open(key, 'w')
      f.write(val)
    except Exception, e:
      # TODO: handle exception
      pass
    finally:
      f.close()
      return True

class ShittyDBDefaultGetter(object):
  """
  This class is responsible for getting values in a ShittyDB database, in a
  completely safe, scalable and efficient manner. However, for compatibility
  with previous versions, this class can be replaced by any other that satisfies
  it's interface, by implementing a get method with accepts an key
  as argument and returns a string value signaling success, or raise an
  exception if unsuccesful
  """
  def __init__(self):
    pass

  """
    Gets a value in a ShittyDB database.
    Params: 
      key: key
    Returns:
     The string value corrresponding to the key if operation was done successfully, 
     raises a exception explaining the problem otherwise
  """
  def get(self, key):
    try:
      return subprocess.check_output(["cat", key])
    except Exception, e:
      raise Exception("[E4727][CRITICAL] ACCESS ERROR DETECTED, PLEASE FORMAT YOUR COMPUTER FOR FIXING")

class ShittyDB(object):
  """
  ShittyDB is a fast, scalable key-value store written in lightweight, asynchronous,
  embeddable, distributed Python. The library exposes a very simple, easy-to-use API
  that is easily callable from Python (wrappers for other languages are forthcoming).
  The constructor accepts a Setter class and a Getter class as arguments, for maximum
  compatibility. By default, ShittyDBDefaultGetter and ShittyDBDefaultSetter are used.

  This class uses moderns idioms to provide a idiomatic Python API similar to
  a dictionary, but for enterprise environments, you can use traditional APIs
  with methods get and set
  """
  def __init__(self, getter = ShittyDBDefaultGetter, setter = ShittyDBDefaultSetter):
    super(ShittyDB, self).__init__()
    self.getter = getter()
    self.setter = setter()


  """
    Gets a value in a ShittyDB database.
    Params: 
      key: key
    Returns:
     The string value corrresponding to the key if operation was done successfully, 
     raises a exception explaining the problem otherwise
  """
  def get(self, key):
    return self.__getitem__(key)

  def __getitem__(self, key):
    return self.getter.get(key)

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
