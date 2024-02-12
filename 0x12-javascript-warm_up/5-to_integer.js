#!/usr/bin/node
const arg1 = process.argv[2];
const numarg1 = parseInt(arg1);
if (Number.isInteger(numarg1)) {
  console.log('My number: ' + numarg1);
} else {
  console.log('Not a number');
}
