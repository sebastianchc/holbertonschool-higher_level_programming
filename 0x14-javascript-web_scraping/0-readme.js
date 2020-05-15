#!/usr/bin/node
const fs = require('fs');
const file = fs.readFile(process.argv[2], 'utf8', function(err, file) {
  if (err) {
    console.log(err);
  } else {
    console.log(file);
  }
});
