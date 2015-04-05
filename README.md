ShittyDB
========

ShittyDB is a fast, scalable key-value store written in lightweight,
asynchronous, embeddable, CAP-full, distributed Python. The library exposes a 
very simple, easy-to-use API that is easily callable from Python, Ruby and 
Node JS (wrappers for other languages are forthcoming).

In Python:

```python
import shittydb
shittydb.set('foo', 'this is really fast')
shittydb.get('foo')
```

In Ruby:

```ruby
require 'shittydb'

ShittyDB.set('foo', 'this is really fast')
ShittyDB.get('foo')
```

In Node.js:

```javascript
var ShittyDB = require("ShittyDB");

var ShittiestDB = new ShittyDB();
ShittiestDB.set('foo', 'this is really fast');
ShittiestDB.get('foo');
```

ShittyDB is certified 100% robust and failsafe with ACID and BASE transactions.

The current release is version 0.0. Please have a look at the source code.
We are accepting all improvements and additions from the open-source
community.

FAQ
---

**Are there performance benchmarks?**

> Those are forthcoming as soon as I can find some that make it look really good.

**What is ShittyDB's story regarding consistency?**

> ShittyDB is strongly consistent and changes are written to disk on each call to `shittydb.set`.

**Can I sacrifice all of my data to the webscale God for ultimate performance?**

> I'm glad you asked. If you're using ShittyDB in Python, use `webscale` mode
> for blazing-fast speed, with the concession that not all of your writes
> are guaranteed to work. Try this:

    sdb = shittydb.ShittyDB()
    print sdb.webscale() # False; ShittyDB is not webscale by default
    sdb.webscale(True) # Make ShittyDB webscale
    sdb['foo'] = 'this is a webscale assignment'
    print sdb['foo'] # What happens here? We don't know! It's webscale!

**Are ShittyDB clients available in other languages?**

> Those are forthcoming.

**Can you change ShittyDB's name?  It's offensive and HR won't let me use it for that reason.**

> No, it's named after my grandfather.

**Does ShittyDB support SQL?**

> No, but you can write an extension to ShittyDB that handles SQL. For example:

    import re
    def shitty_sql(sql):
        match = re.match("SELECT \\* FROM ([a-z])", sql).group(1)
        return shittydb.get(match)

> Usage:

    shittydb.set("foo", "abc")
    shitty_sql("SELECT * FROM foo")

**How do you distribute ShittyDB?**

> What?

**You said up there it was a distributed key-value store.**

> Sorry, I must have misspoken.
