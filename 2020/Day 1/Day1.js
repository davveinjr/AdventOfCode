const fs = require("fs");

const data = fs.readFileSync("day1.txt", "utf-8").split("\n");

////part 1
let p1Total = 0;

for (let i = 0; i < data.length; i++) {
  for (let j = 1; j < data.length; j++) {
    if (Number(data[i]) + Number(data[j]) === 2020) {
      p1Total = Number(data[i]) * Number(data[j]);
      break;
    }
  }
}

console.log(`Part 1 answer: ${p1Total}`);

////part 2

let p2Total = 0;

for (let i = 0; i < data.length; i++) {
  for (let j = 1; j < data.length; j++) {
    for (let k = 2; k < data.length; k++) {
      if (Number(data[i]) + Number(data[j]) + Number(data[k]) === 2020) {
        p2Total = Number(data[i]) * Number(data[j]) * Number(data[k]);
        break;
      }
    }
  }
}

console.log(`Part 2 answer: ${p2Total}`);
