#!/usr/bin/node

const process = require('process');
const arg1 = process.argv[2];
const arg2 = process.argv[3];
const arg1Parsed = parseInt(arg1);
const arg2Parsed = parseInt(arg2);

function add (a, b) {
  console.log(a + b);
}

add(arg1Parsed, arg2Parsed);
