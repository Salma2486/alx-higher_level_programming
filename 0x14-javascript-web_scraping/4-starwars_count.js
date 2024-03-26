#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];
const characterId = '18';
request.get(apiUrl, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  const data = JSON.parse(body);
  const filmsWithWedge = data.results.filter(film => 
    film.characters.some(characterUrl => characterUrl.endsWith(`/${characterId}/`))
  );
  console.log(filmsWithWedge.length);
});
