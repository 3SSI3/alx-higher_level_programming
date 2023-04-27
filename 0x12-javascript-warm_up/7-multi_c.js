#!/usr/bin/node

let times = parseInt(process.argv[2]);
if (!isNaN(times)) {
  while (times > 0) {
    console.log('C is fun');
    times -= 1;
  }
} else {
  console.log('Missing number of occurrences');
}