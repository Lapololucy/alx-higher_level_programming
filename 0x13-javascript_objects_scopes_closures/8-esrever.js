#!/usr/bin/node
exports.esrever = function (list) {
  return list.map((_, idx, arr) => arr[arr.length - 1 - idx]);
};
