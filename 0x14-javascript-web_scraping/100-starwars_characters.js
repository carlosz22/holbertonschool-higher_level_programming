#!/usr/bin/node

const request = require('request');
const idToFind = process.argv[2];
const url = 'https://swapi.co/api/films/' + idToFind + '/';

request(url, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(body).characters;

    for (let i = 0; i < data.length; i++) {
      getCharacterName(data[i]);
    }
  }
});

function getCharacterName (url) {
  request(url, function (err, res, body) {
    if (err) {
      console.log(err);
    } else {
      console.log(JSON.parse(body).name);
    }
  });
}
