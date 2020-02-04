#!/usr/bin/node

const process = require('process');
const arg1 = process.argv[2];
const arg1Parsed = parseInt(arg1);
if (arg1Parsed) {
  console.log('My number: ' + arg1);
} else {
  console.log('Not a number');
}
