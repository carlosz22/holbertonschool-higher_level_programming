#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const idToFind = 18;
const urlToFind = 'https://swapi.co/api/people/' + idToFind + '/';

request(url, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(body).results;
    let countCharacter = 0;

    for (let i = 0; i < data.length; i++) {
      const countMovie = data[i].characters.filter(x => x === urlToFind).length;
      countCharacter += countMovie;
    }
    console.log(`${countCharacter}`);
  }
});
