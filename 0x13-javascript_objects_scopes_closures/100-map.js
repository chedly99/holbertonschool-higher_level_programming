#!/usr/bin/node
const list = require('./100-data').list;
let mul = 0;
const newList = list.map(x => x * mul++);
console.log(list);
console.log(newList);
