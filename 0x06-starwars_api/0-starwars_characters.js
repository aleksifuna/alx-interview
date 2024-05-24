#!/usr/bin/node

const request = require('request');

request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], (error, response, body) => {
  if (error) throw error;
  const actors = JSON.parse(body).characters;
  displayInOrder(actors, 0);
});

function displayInOrder (actors, index) {
  if (index === actors.length) return;
  request(actors[index], (error, response, body) => {
    if (error) throw error;
    console.log(JSON.parse(body).name);
    displayInOrder(actors, index + 1);
  });
}
