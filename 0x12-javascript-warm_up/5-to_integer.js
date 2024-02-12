#!/usr/bin/node
let arg1 = process.argv[2];
numarg1 = parseInt(arg1);
if (Number.isInteger(numarg1)) {
  console.log('My number: ' + numarg1)
} else {
  console.log('Not a number');
}
