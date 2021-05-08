#!/usr/bin/node

const dict = require('./101-data').dict;
const newDict = {};
for (const i in dict) {
  /* i is the key */
  if (newDict[dict[i]] === undefined) {
    newDict[dict[i]] = [];
  }
  newDict[dict[i]].push(i);
}
console.log(newDict);
