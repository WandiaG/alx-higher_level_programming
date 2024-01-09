#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  /**
   * @property {method} print - prints the rectangle using the character X
   * @returns void
   */
  print () {
    for (let i = 0; i < this.height; i++) {
      let s = '';
      for (let j = 0; j < this.width; j++) {
        s += 'X';
      }
      console.log(s);
    }
  }

  /**
   * @property {method} rotate - rotates the rectangle by exchangeing width and the height.
   * @returns void
   */
  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  /**
   * @property {method} double - increases the rectangle by 2.
   * @returns void
   */
  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
