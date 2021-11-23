const fs = require("fs");

const data = fs.readFileSync("Day3.txt", "utf-8").split("\n");

//part 1

let collisions = 0;
let x = 0;

for (let i = 0; i < data.length; i++) {
  let mapWidth = data[i].length;
  let row = data[i];

  if (row[x] === "#") {
    collisions++;
  }
  x = (x + 3) % mapWidth;
}

console.log(`Part 1 Answer: ${collisions}`);
//part 2
function checkCollision(map, horizontal, vertical) {
  let collision = 0;
  let x = 0;

  for (let i = 0; i < map.length; i = i + vertical) {
    let row = map[i];
    let mapWidth = map[i].length;

    if (row[x] === "#") {
      collision++;
    }
    x = (x + horizontal) % mapWidth;
  }

  return collision;
}

console.log(
  `Part 2 Answer: ${
    checkCollision(data, 1, 1) *
    checkCollision(data, 3, 1) *
    checkCollision(data, 5, 1) *
    checkCollision(data, 7, 1) *
    checkCollision(data, 1, 2)
  }`
);
