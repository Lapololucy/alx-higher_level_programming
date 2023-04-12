#!/usr/bin/node
// Import the Rectangle class
const Rectangle = require('./4-rectangle.js');

// Define the Square class that inherits from Rectangle
class Square extends Rectangle {
  constructor(size) {
    // Call the constructor of Rectangle with the size argument for both width and height
    super(size, size);
  }
}

// Export the Square class
module.exports = Square;

