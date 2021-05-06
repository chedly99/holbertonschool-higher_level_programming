#!/usr/bin/node

const squareSize = process.argv[2];
let Fill = '';
if (isNaN(squareSize) === true) {
  console.log('Missing size');
} else {
  for (let i = 0; i < squareSize; i++) {
    Fill += 'X';
  }
  for (let i = 0; i < squareSize; i++) {
    console.log(Fill);
  }
}
