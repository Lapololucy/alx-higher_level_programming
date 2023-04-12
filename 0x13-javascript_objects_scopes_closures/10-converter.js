#!/usr/bin/node
exports.converter = function (base) {
  return function (number) {
    return Number(number).toString(base);
  };
};
