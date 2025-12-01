count = 0;
dial = 50;

``.split("\n")
  .map((inst) => Number(inst.slice(1)) * (inst.startsWith("L") ? -1 : 1))
  .forEach((inst) => {
	if(inst < 0){
		for (let i = 0; i < Math.abs(inst); i++) {
			dial -= 1;
			if(dial < 0) dial += 100;
			if (dial == 0) count += 1;
		}
	} else {
		for (let j = 0; j < inst; j++) {
			dial += 1;
			if(dial >= 100) dial -= 100;
			if (dial == 0) count += 1;
		}
	}
  });

console.log(count);
