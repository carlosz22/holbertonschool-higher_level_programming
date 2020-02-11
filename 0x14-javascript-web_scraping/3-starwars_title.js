#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const url = 'http://swapi.co/api/films/';

request(url + id, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    console.log(`${JSON.parse(body).title}`);
  }
});
