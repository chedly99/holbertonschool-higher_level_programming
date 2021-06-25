#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
request(url, function (err, response, body) {
  if (err) { console.log(err); } else {
    const done = {};
    for (const i of JSON.parse(body)) {
      if (i.completed === true) {
        if (done[i.userId] === undefined) {
          done[i.userId] = 1;
        } else { done[i.userId] = done[i.userId] + 1; }
      }
    }
    console.log(done);
  }
});
