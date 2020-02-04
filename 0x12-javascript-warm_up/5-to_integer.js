#!/usr/bin/node

const process = require('process');
const arg1 = process.argv[2];
const arg1Parsed = parseInt(arg1);
if (arg1Parsed) {
  console.log('My number: ' + arg1Parsed);
} else {
  console.log('Not a number');
}
