#!/usr/bin/node
const Base = require('./5-square');
class Square extends Base {
  charPrint (chr = 'X') {
    for (let i = 0; i < this.height; i++) {
      console.log(chr.repeat(this.width));
    }
  }
}
module.exports = Square;
