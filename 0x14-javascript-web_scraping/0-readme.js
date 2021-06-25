#!/usr/bin/node

const process = require('process');
const file = process.argv[2];
const fs = require('fs');
fs.readFile(file, 'utf-8', (err, data) => {
  if (err) { console.log(err); } else {
    console.log(data);
  }
});
