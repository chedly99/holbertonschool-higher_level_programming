#!/usr/bin/node

const request = require('request');
const ar = [];
const url = process.argv[2];
request(url, function (err, response, body) {
  if (err) { console.log(err); } else if (response.statusCode === 200) {
    let count = 0;
    for (const c of JSON.parse(body).results) {
      ar.push(c.characters);
    }
    for (let i = 0, len = ar.length; i < len; i++) {
      for (let j = 0, len2 = ar[i].length; j < len2; j++) {
        if (ar[i][j] === 'https://swapi-api.hbtn.io/api/people/18/') { count++; }
      }
    }
    console.log(count);
  } else { console.log(''); }
});
