#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (err, res, cont) {
  if (!err) {
    let count = 0;
    const json = JSON.parse(cont);
    const list = json.results;
    for (const movie of list) {
      const characters = movie.characters;
      for (const character of characters) {
        if (character.search('18') !== -1) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
