#!/usr/bin/node
const request = require('request');

request(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}/`, (error, _, body) => {
  if (error) {
    console.error('Error:', error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
