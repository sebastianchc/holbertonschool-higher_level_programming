#!/usr/bin/node
const list = require('./100-data').list;
const newList = list.map(function (num, index) {
  return index * num;
});
console.log(list);
console.log(newList);
