lines = open(0).read().strip().splitlines()

byte_length = len(lines[0]) - 1
def is_majority_true(lines, index):
	return sum(int(line[index]) for line in lines) >= len(lines)/2
gamma = sum(2**i * is_majority_true(lines,-i-2) for i in range(byte_length))
epsilon = 2**byte_length - 1 - gamma

def filter_lines(lines,index,condition):
	return lines[0] if len(lines) == 1 else filter_lines([e for e in lines if (int(e[index]) ^ is_majority_true(lines,index)) ^ condition ], index+1, condition)
oxygen = int(filter_lines(lines,0,1),2)
carbon = int(filter_lines(lines,0,0),2)

print("Part 1: {:d}".format(epsilon*gamma))
print("Part 2: {:d}".format(oxygen*carbon))