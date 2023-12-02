const fs = require("fs");

const data = fs.readFileSync(process.argv[2], "utf-8");

const grid = data.trim().split("\n");

const R = grid.length;
const C = grid[0].length;

const east = [];
const south = [];


for (let r = 0; r < R; r++) {
    for (let c = 0; c < C; c++) {
        if (grid[r][c] == ">") east.push([r, c]);
        else if (grid[r][c] == "v") south.push([r, c]);
    }
}

const taken = grid.map((row) => [...row].map((char) => char != "."));

function move(herd, dr, dc) {
  const m = herd.filter((x) => !taken[(x[0] + dr) % R][(x[1] + dc) % C]);
  for (const x of m) {
    let [r, c] = x;

    x[0] = (r + dr) % R;
    x[1] = (c + dc) % C;

    taken[r][c] = false;
    taken[x[0]][x[1]] = true;
  }

  return m.length;
}

for (let i = 1; ; i++) {
  if (!move(east, 0, 1) & !move(south, 1, 0)) {
    console.log(i);
    break;
  }
}
