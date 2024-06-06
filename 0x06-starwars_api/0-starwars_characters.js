#!/usr/bin/node
const req = require('request');
const id = process.argv[2];
const options = {
  url: 'https://swapi-api.hbtn.io/api/films/' + id,
  method: 'GET'
};

req(options, function (error, response, body) {
  if (!error) {
    const characters = JSON.parse(body).characters;
    printchars(characters, 0);
  }
});

function printchars (characters, index) {
  req(characters[index], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (index + 1 < characters.length) {
        printchars(characters, index + 1);
      }
    }
  });
}
