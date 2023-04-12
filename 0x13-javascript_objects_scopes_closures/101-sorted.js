#!/usr/bin/node
const dict = require('./101-data').dict;

const newDict = {};

for (const [key, val] of Object.entries(dict)) {
  newDict[val] ? newDict[val].push(key) : (newDict[val] = [key]);
}
console.log(newDict);
