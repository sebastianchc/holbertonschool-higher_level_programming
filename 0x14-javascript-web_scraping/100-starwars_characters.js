#!/usr/bin/node
const request = require('request');
request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], function (err, res, cont) {
  if (!err) {
    const json = JSON.parse(cont);
    const characters = json.characters;
    for (const character of characters) {
      request(character, function (err, res, cont) {
        if (!err) {
          const json = JSON.parse(cont);
          console.log(json.name);
        }
      });
    }
  }
});
