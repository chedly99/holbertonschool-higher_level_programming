#!/usr/bin/node

const request = require('request');
const endpoint = 'https://swapi-api.hbtn.io/api/films/';
const filter = process.argv[2];
const url = endpoint + filter;

request(url, function (error, response, body) {
  if (error) { return console.log(error); } else {
    for (const star of JSON.parse(body).characters) {
      request(star, function (err, res, bod) {
        if (err) { return console.log(err); }
        console.log(JSON.parse(bod).name);
      });
    }
  }
});
