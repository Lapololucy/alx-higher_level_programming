#!/usr/bin/node
/**
 * check if the correct number of the arguments have been provided
 * get the file paths from command line arguments
 * concatenate the files
 */
#!/usr/bin/node
const fs = require('fs');
const a = fs.readFileSync(process.argv[2], 'utf8');
const b = fs.readFileSync(process.argv[3], 'utf8');
fs.writeFileSync(process.argv[4], a + b);
