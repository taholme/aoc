let inp =
  ``
    .split("\n")
    .map((line) => line.split(""));

const row_length = inp[0].length;
const col_length = inp.length;

let sum = 0;
let nums = [];

for (let i = row_length - 1; i >= 0; i--) {
  let col = [];
  for (let j = 0; j < col_length; j++) {
    if (inp[j][i] == " ") {
      if (j == col_length - 1 && Number(col.join("")) > 0) {
        nums.push(Number(col.join("")));
      }
    } else if (inp[j][i] == "+") {
      nums.push(Number(col.join("")));
      sum += nums.reduce((a, b) => a + b, 0);
      nums = [];
    } else if (inp[j][i] == "*") {
      nums.push(Number(col.join("")));
      sum += nums.reduce((a, b) => a * b, 1);
      nums = [];
    } else {
      col.push(inp[j][i]);
    }
  }
}

console.log(sum);
