#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.elog(error);
  }
  const data = JSON.parse(body);
  const films = data.results.filter(film => film.characters.includes('18'));
  console.log(films.length);
});