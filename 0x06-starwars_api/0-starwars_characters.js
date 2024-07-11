#!/usr/bin/node
const request = require('request');
const BASE_URI = 'https://swapi-api.alx-tools.com/api';

if (process.argv.length > 2) {
  request(
    `${BASE_URI}/films/${process.argv[2]}`,
    { json: true },
    (error, res, body) => {
      if (error) {
        console.log(error);
      }

      if (res.statusCode !== 200) {
        return console.error(
          `Failed to fetch movie details: ${res.statusCode}`
        );
      }

      const characters = body.characters;

      for (const character of characters) {
        request(character, { json: true }, function (error, res, body) {
          if (error) {
            console.log(error);
          }

          if (res.statusCode !== 200) {
            return console.error(
              `Failed to fetch character details: ${res.statusCode}`
            );
          }

          console.log(body.name);
        });
      }
    }
  );
}
