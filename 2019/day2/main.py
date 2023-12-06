program = [int(x) for x in open(0).read().split(',')]

program[1] = 12
program[2] = 2

for i in range(0,len(program),4):
    match program[i]:
        case 99:
            break
        case 1:
            program[program[i+3]] = program[program[i+1]] + program[program[i+2]]
        case 2:
            program[program[i+3]] = program[program[i+1]] * program[program[i+2]]

print(program[0])