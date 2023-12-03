const fs = require("fs");
const data = fs.readFileSync(process.argv[2], "utf-8");

const lines = data.trim().split("\n"); //may contain crlf

t = 0

for(line of lines){
    t += line
}

console.log(t)