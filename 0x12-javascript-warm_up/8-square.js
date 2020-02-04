#!/usr/bin/node

const process = require('process');
const arg1 = process.argv[2];
const arg1Parsed = parseInt(arg1);
if (arg1Parsed) {
  for (let i = 0; i < arg1Parsed; i++) {
    console.log('X'.repeat(arg1Parsed));
  }
} else {
  console.log('Missing size');
}
