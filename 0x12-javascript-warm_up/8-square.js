#!/usr/bin/node
// prints a square
const args = process.argv.slice(2);
if (args.length === 0 || isNaN(args[0])) {
// if 1st arg can't be converted to an int print "Missing size"
  console.log('Missing size');
} else {
  const x = Number(process.argv[2]);
  for (let a = 0; a < x; a++) {
    console.log('X'.repeat(x));
  }
}
