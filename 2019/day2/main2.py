from itertools import product
from copy import copy
program = [int(x) for x in open(0).read().split(',')]
programcopy = copy(program)



for x, y in product(list(range(100)), repeat=2):
    program = copy(programcopy)
    program[1] = x
    program[2] = y
    for i in range(0,len(program),4):
        match program[i]:
            case 99:
                continue
            case 1:
                if program[i+3] > len(program) or program[i+1] > len(program) or program[i+2] > len(program):
                    continue
                program[program[i+3]] = program[program[i+1]] + program[program[i+2]]
            case 2:
                if program[i+3] > len(program) or program[i+1] > len(program) or program[i+2] > len(program):
                    continue
                program[program[i+3]] = program[program[i+1]] * program[program[i+2]]
    if program[0] == 19690720:
        print(100*x + y)
        exit()