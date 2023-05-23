#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

try {
  request(url, function (error, response, body) {
    if (error) {
      console.error('error:', error);
    } else {
      console.log('code:', response && response.statusCode);
    }
  });
} catch (err) {
  console.log(`${err}`);
}
