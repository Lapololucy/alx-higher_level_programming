#!/usr/bin/node
/**
 * import thr Rectangle class
 * Define the square class that inherits from Rectangle
 * call the constructor of the Rectangle with the size arguement for both width
 * Export the square class
 */

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
