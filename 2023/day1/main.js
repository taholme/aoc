const fs = require("fs");
const data = fs.readFileSync(process.argv[2], "utf-8");

const inp = data.trim().split("\n");