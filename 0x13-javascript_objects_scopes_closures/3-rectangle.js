#!/usr/bin/node

class Rectangle {
  counstructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.length = h;
    }
  }

  print () {
    for (let u = 0; u < this.height; u++) {
      console.log('X'.repeat(this.width));
    }
  }
}

module.exports = Rectangle;
