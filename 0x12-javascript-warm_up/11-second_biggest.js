#!/usr/bin/node

let myArgs = process.argv;
if (myArgs.length >= 4) {
  myArgs = myArgs.sort((a, b) => a - b);
  console.log(myArgs[myArgs.length - 2]);
} else {
  console.log(0);
}
