const fs = require("fs");

const data = fs.readFileSync("Day4.txt", "utf-8").split("\n\n");

const validKeys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"];
const validEyeColors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"];
const hexLegend = "0123456789abcdef";

let validCount_part1 = 0;
let validCount_part2 = 0;
//let passports_part2 = {};

for (let i = 0; i < data.length; i++) {
  const separators = [" ", "\n"];
  const passport = data[i].split(new RegExp(separators.join("|"), "g"));

  let isValid = checkValidity(passport);

  if (isValid) {
    validCount_part1++;
  }
}

console.log(`Part 1 Answer: ${validCount_part1}`);

//// part2

function checkValidity(passport) {
  let counter = 0;
  for (let i = 0; i < passport.length; i++) {
    let [key, value] = passport[i].split(":");

    if (validKeys.includes(key)) {
      counter++;
    }
  }
  if (counter >= validKeys.length) {
    return true;
  } else {
    return false;
  }
}

for (let i = 0; i < data.length; i++) {
  const separators = [" ", "\n"];
  const passport = data[i].split(new RegExp(separators.join("|"), "g"));

  let valid = checkValidity(passport);

  if (valid) {
    let valueCheck = true;

    for (let i = 0; i < passport.length; i++) {
      let [key, value] = passport[i].split(":");

      switch (key) {
        case "byr":
          let byr = parseInt(value);

          if (byr >= 1920 && byr <= 2002) {
            break;
          } else {
            valueCheck = false;
            break;
          }
        case "iyr":
          let iyr = parseInt(value);

          if (iyr >= 2010 && iyr <= 2020) {
            break;
          } else {
            valueCheck = false;
            break;
          }
        case "eyr":
          let eyr = parseInt(value);

          if (eyr >= 2020 && eyr <= 2030) {
            break;
          } else {
            valueCheck = false;
            break;
          }
        case "hgt":
          if (value.includes("cm")) {
            value = value.replace("cm", "");
            let hgt = parseInt(value);
            if (hgt > 193 || hgt < 150) {
              valueCheck = false;
              break;
            }
          } else if (value.includes("in")) {
            value = value.replace("in", "");
            let hgt = parseInt(value);
            if (hgt > 76 || hgt < 59) {
              valueCheck = false;
              break;
            }
          } else {
            valueCheck = false;
            break;
          }
        case "hcl":
          if (value[0] != "#") {
            valueCheck = false;
            break;
          } else {
            value = value.replace("#", "");
            if (value.length === 6) {
              for (let j = 0; j < value.length; j++) {
                if (hexLegend.includes(value[j])) {
                  continue;
                } else {
                  valueCheck = false;
                  break;
                }
              }
            } else {
              valueCheck = false;
              break;
            }
          }
        case "ecl":
          if (validEyeColors.includes(value)) {
            break;
          } else {
            valueCheck = false;
            break;
          }
        case "pid":
          if (value.length === 9) {
            if (!isNaN(value)) {
              break;
            } else {
              valueCheck = false;
              break;
            }
          } else {
            valueCheck = false;
            break;
          }
      }

      if (valueCheck === false) {
        break;
      }
    }

    if (valueCheck) {
      validCount_part2++;
    }
  }
}

console.log(`The answer to part 2 is: ${validCount_part2}`);
