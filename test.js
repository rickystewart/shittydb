var ShittyDB = require("./shittydb");

db = new ShittyDB();
db.set('foo', 'this is really proper');
console.log(db.get('foo'));