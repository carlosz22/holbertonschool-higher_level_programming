#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const fileName = process.argv[3];

request(url, 'utf-8', function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    writeToFile(fileName, body);
  }
});

function writeToFile (fileName, content) {
  fs.writeFile(fileName, content, 'utf-8', function (err, data) {
    if (err) {
      console.log(err);
    }
  });
}
