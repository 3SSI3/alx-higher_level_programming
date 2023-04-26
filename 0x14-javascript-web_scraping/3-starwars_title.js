#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/:id' + process.argv[2];
request(url, function (err, response, body) {
console.log(err || JSON.parse(body).title);
});