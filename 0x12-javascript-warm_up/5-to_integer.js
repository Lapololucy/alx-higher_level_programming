#!/usr/bin/node
if (isNaN(process.argv[2]) || process.argv[2] === underfined) {
	console.log('Not a number');
} else {
	console.log('My number:' parseInt(process.argv[2]));
}
