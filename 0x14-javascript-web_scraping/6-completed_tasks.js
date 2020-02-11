#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, function (err, res, body) {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(body);
    const userDict = {};
    for (let i = 0; i < data.length; i++) {
      console.log(i);
      if (userDict[data[i].userId] && data[i].completed) {
        userDict[data[i].userId]++;
      } else if (data[i].completed) {
        userDict[data[i].userId] = 1;
      }
    }
    console.log(userDict);
  }
});
