#!/usr/bin/node

const files = require('fs');
const varA = process.argv[2];
const varB = process.argv[3];
const varC = process.argv[4];
const fA = files.readFileSync(varA, 'utf-8');
const fB = files.readFileSync(varB, 'utf-8');
files.writeFileSync(varC, fA + fB);
