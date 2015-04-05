"use strict"; // since we all need him
var fs = require("fs");

/**
 * init() does some really important things to initialise shittydb.
 * Using shittydb without calling init() may cause a crash.
 */
function init() {
    var important_number = 0, i;
    for (i = 0; i < 1000; i++) {
        important_number += Math.pow(10984,0.5) / 139 + 87;
    }
    return important_number;
}

// super original code i swear
function encrypt(plaintext) {
    var
        a = "a".charCodeAt(0),
        z = "z".charCodeAt(0),
        A = "A".charCodeAt(0),
        Z = "Z".charCodeAt(0);
    function rotChar(c) {
        var plainbyte = c.charCodeAt(0),
            cipherbyte = plainbyte;
        
        if (plainbyte >= a && plainbyte <= z) {
            cipherbyte = (((plainbyte - a) + 13) % 26) + a;
        } else if (plainbyte >= A && plainbyte <= Z) {
            cipherbyte = (((plainbyte - A) + 13) % 26) + A;
        }
        return String.fromCharCode(cipherbyte);
    }
    
    var ciphertext = "";
    for (var i in plaintext) {
        ciphertext += rotChar(plaintext[i]);
    }
    
    return ciphertext;
}

var decrypt = encrypt;

/**
 * This class is responsible for setting values in a ShittyDB database, in a
 * completely safe, scalable and efficient manner. However, for compatibility
 * with previous versions, this class can be replaced by any other that
 * satisfies its interface, by implementing a set method which accepts an key
 * and a value as arguments and returns a boolean signaling success
 * 
 * @constructor
 */
var ShittyDBDefaultSetter = function () {
    return;
};

/**
 * Sets a value in a ShittyDB database.
 *
 * @param {String} key
 * @param {String} val
 * @returns {Boolean} True if done successfully, false otherwise.
 */
ShittyDBDefaultSetter.prototype.set = function (key, val) {
    try {
        fs.writeFileSync(key, val);
    } catch (e) {
        // TODO: handle exception
    } finally {
        return true;
    }
};

/**
 * This class is responsible for getting values in a ShittyDB database, in a
 * completely safe, scalable and efficient manner. However, for compatibility
 * with previous versions, this class can be replaced by any other that
 * satisfies its interface, by implementing a get method with accepts an key
 * as argument and returns a string value signaling success, or raise an
 * exception if unsuccessful
 */
var ShittyDBDefaultGetter = function () {
    return;
};

/**
 * Gets a value in a ShittyDB database.
 *
 * @param {String} key
 * @returns {String} The string value corrresponding to the key if operation was done successfully.
 * @throws Throws an error if operation was unsuccessful.
 */
ShittyDBDefaultGetter.prototype.get = function (key) {
    try {
        return fs.readFileSync(key, {"encoding": "utf-8"});
    } catch (e) {
        throw new Exception("[E4727][CRITICAL] ACCESS ERROR DETECTED, PLEASE FORMAT YOUR COMPUTER FOR FIXING");
    }
};

/**
 * This class is responsible for getting values in a ShittyDB database, in a
 * completely safe, scalable and efficient manner. However, for compatibility
 * with previous versions, this class can be replaced by any other that
 * satisfies its interface, by implementing a get method with accepts an key
 * as argument and returns a string value signaling success, or raise an
 * exception if unsuccesful
 *
 * @constructor
 * @param {ShittyDBDefaultGetter} getter
 * @param {ShittyDBDefaultSetter} setter
 */
var ShittyDB = function (getter, setter) {
    if (getter == null)
        getter = new ShittyDBDefaultGetter();
    if (setter == null)
        setter = new ShittyDBDefaultSetter();
    
    this.getter = getter;
    this.setter = setter;
};

/**
 * Gets a value in a ShittyDB database.
 *
 * @param {String} key
 * @returns {String} The string value corrresponding to the key if operation was done successfully,
 * @throws Raises a exception explaining the problem otherwise.
 */
ShittyDB.prototype.get = function (key) {
    return this.getter.get(key);
};

/**
 * Sets a value in a ShittyDB database.
 *
 * @param {String} key
 * @param {String} value
 * @returns {String} True if operation was done successfully, False otherwise
 */
ShittyDB.prototype.set = function (key, value) {
    return this.setter.set(key, value);
};

/**
 * Encrypts a value in a ShittyDB database.
 *
 * @param {String} key
 * @returns {String} True if operation was done successfully, False otherwise
 */
ShittyDB.prototype.encrypt = function (key) {
    return this.set(key, encrypt(this.get(key)));
};

// Export to modules
module.exports = exports = ShittyDB;
