#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const characterId = '18';
request(url, function (error, response, body) {
  if (!error) {
    const films = JSON.parse(body).results;
    let count = 0;

    films.forEach((films) => {
      films.characters.forEach((character) => {
        if (character.includes(characterId)) {
          count += 1;
        }
      });
    });
    console.log(count);
  }
});
