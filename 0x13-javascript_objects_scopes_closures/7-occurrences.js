#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let counter = 0;
  list.forEach((cur) => {
    if (cur === searchElement) counter++;
  });
  return counter;
};
