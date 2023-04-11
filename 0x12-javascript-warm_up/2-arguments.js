#!/usr/bin/node
const argc = process.argv.length;
if (argc === 2) {
  console.log('No argument');
} else if (argc === 3) {
  console.log('Argument found');
} else if (argc > 3) {
  console.log('Arguments found');
}
