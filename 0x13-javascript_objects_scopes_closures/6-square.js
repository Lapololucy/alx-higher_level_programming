#!/usr/bin/node
/**
 * import the Square class
 * Define the square class that inherits from BaseSquare
 * use the character X if c is undefined
 * print the square using the character c
 */
const BaseSquare = require('./5-square.js');

class Square extends BaseSquare {
  charPrint (c) {
    if (!c) this.print();
    else {
      for (let i = 0; i < this.width; i++) console.log(c.repeat(this.height));
    }
  }
}

module.exports = Square;
