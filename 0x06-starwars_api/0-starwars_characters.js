#!/usr/bin/node
const request = require("request");
const BASE_URI = "https://swapi-api.alx-tools.com/api";

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

      const charactersUrl = body.characters;
      const characterNames = charactersUrl.map(
        (url) =>
          new Promise((resolve, reject) => {
            request(url, { json: true }, (err, _, character) => {
              if (err) {
                reject(err);
              }
              resolve(character.name);
            });
          })
      );

      Promise.all(characterNames)
        .then((names) => console.log(names.join("\n")))
        .catch((err) => console.error(err));
    }
  );
}
