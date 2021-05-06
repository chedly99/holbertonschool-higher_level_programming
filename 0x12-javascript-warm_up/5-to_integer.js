#!/usr/bin/node

const Variable = process.argv[2];
if (isNaN(Variable) === true) {
  console.log('Not a number');
} else {
  console.log('My number: ' + Variable);
}
