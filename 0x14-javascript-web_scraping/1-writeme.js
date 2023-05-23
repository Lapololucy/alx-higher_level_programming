#!/usr/bin/node
/* Write a string to a file */

const fs = require('fs');
const filename = process.argv[2];
const text = process.argv[3];
fs.writeFile(filename, text, 'utf8', (err) => {
  if (err) console.log(err);
});
