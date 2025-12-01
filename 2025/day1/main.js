count = 0;
dial = 50;

``.split('\n').forEach((inst) => {
  num = Number(inst.slice(1)) * (inst.startsWith('L') ? -1 : 1);
	dial += num
	dial = dial % 100;
  if (dial === 0) count += 1;
})

console.log(count);
