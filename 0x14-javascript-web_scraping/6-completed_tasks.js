#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (err, res, cont) {
  if (!err) {
    const json = JSON.parse(cont);
    const completes = {};
    for (const info of json) {
      if (info.completed) {
        if (!completes[info.userId]) {
          completes[info.userId] = 0;
        }
        completes[info.userId]++;
      }
    }
    console.log(completes);
  }
});
