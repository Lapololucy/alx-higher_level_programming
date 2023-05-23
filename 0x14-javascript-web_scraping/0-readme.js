#!/usr/bin/node
/* Reads and Prints the contents of a file */

const fs = require('fs');
const filename = process.argv[2];
fs.readFile(filename, 'utf8', (err, data) => {
  if (err) console.log(err);
  else console.log(data.toString());
});
