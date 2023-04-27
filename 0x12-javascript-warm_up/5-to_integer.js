#!/usr/bin/node
// prints My number: <first argument converted in integer> if the first argument can be converted to an integer
const parsedVal = parseInt(process.argv[2]);

if(!isNaN(parsedVal)) {
  console.log(`My number: ${parsedVal}`);
} else {
console.log('Not a number');
}