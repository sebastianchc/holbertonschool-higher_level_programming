#!/usr/bin/node
exports.esrever = function (list) {
  let prev = list.length - 1;
  let next = 0;
  while (next < list.length / 2) {
    [list[next], list[prev]] = [list[prev], list[next]];
    next++;
    prev--;
  }
  return list;
};
