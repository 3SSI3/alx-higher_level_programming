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
	     let s = '';
      for (let j = 0; j < this.width; j++) {
        s += 'X';
      }
	    console.log(s);
    }
  }
}

module.exports = Rectangle;
