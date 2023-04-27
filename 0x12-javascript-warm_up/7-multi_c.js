#!/usr/bin/node

const parsedVal = parseInt(process.argv[2]);
if (isNaN(parsedVal)) {
  console.log('Missing number of occurences');
} else {
  for (let a = 0; a < parsedVal; a++) {
    console.log('C is fun');
  }
}
