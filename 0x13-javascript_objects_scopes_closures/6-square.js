#!/usr/bin/node

const SquareCons = require('./5-square');

class Square extends SquareCons {
  charPrint (c) {
    for (let i = 0; i < this.height; i++) {
      if (c == null) {
        console.log('X'.repeat(this.width));
      } else {
        console.log(c.repeat(this.width));
      }
    }
  }
}

module.exports = Square;
