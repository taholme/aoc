inp = ``.split('\n').map((line) => line.trim().split(/\s+/))

ops = inp.pop()

transposed_inp = inp[0].map((_, colIndex) => inp.map(row => row[colIndex]))

const mult = (a,b) => (a*b)
const add = (a,b) => (a+b)

transposed_inp.map((column, i) => column.map(Number).reduce((curr, acc) => ops[i] == '*' ? mult(curr, acc) : add(curr, acc), (ops[i] == '*' ? 1 : 0))).reduce((curr, acc) => curr + acc, 0)
