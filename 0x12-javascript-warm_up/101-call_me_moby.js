#!/usr/bin/node

function repeat(x, theFunction) {
  for (let i = 0; i < x; i++) {
    theFunction();
  }
}

module.exports = repeat;
