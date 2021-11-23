const fs = require("fs");

data = fs.readFileSync("Day2.txt", "utf-8").split("\n");

//part 1

let p1Total = 0;

for (let i = 0; i < data.length; i++) {
  let [range, target, password] = data[i].split(" ");
  let [min, max] = range.split("-");
  target = target.replace(":", "");
  min = parseInt(min);
  max = parseInt(max);

  let occurances = 0;
  for (let j = 0; j < password.length; j++) {
    if (password[j] === target) {
      occurances++;
    }
  }

  if (occurances >= min && occurances <= max) {
    p1Total++;
  }
}

console.log(`Part 1 answer: ${p1Total}`);

//part2

let p2Total = 0;

for (let i = 0; i < data.length; i++) {
  let [range, target, password] = data[i].split(" ");
  let [lower, upper] = range.split("-");
  target = target.replace(":", "");
  lower = parseInt(lower);
  upper = parseInt(upper);

  if (
    (password[lower - 1] === target && password[upper - 1] != target) ||
    (password[lower - 1] != target && password[upper - 1] === target)
  ) {
    p2Total++;
  }
}

console.log(`Part 2 answer: ${p2Total}`);
