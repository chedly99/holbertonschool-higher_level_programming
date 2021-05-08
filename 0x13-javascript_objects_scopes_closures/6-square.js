#!/usr/bin/node

const SquarePrev = require('./5-square');
module.exports = class Square extends SquarePrev {
  charPrint (c) {
    if (c === undefined) {
      return this.print();
    } else {
      let space2 = '';
      for (let i = 0; i < this.width; i++) {
        space2 += c;
      }
      for (let i = 0; i < this.height; i++) {
        console.log(space2);
      }
    }
  }
};
