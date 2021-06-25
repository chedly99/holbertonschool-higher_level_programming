#!/usr/bin/node

const request = require('request');
const endpoint = 'https://swapi-api.hbtn.io/api/films/';
const filter = process.argv[2];
const url = endpoint + filter;
const listx = [];
const listname = [];
let count = 0;
request(url, function (error, response, body) {
  if (error) { return console.log(error); } else {
    for (let m = 0; m < JSON.parse(body).characters.length; m++) {
      listx.push(JSON.parse(body).characters[m]);
    }
  }
  for (let k = 0; k < listx.length; k++) {
    request(listx[k], function (e, r, b) {
      if (e) { return console.log(e); }
      listname.push(JSON.parse(b).name);
      // console.log(JSON.parse(b).name);
      // console.log(listname);
      count++;
      if (count === listx.length) {
        for (let x = 0; x < listname.length; x++) { console.log(listname[x]); }
      }
    // console.log(listname);}
    });
    // console.log(listname);
  }
});
