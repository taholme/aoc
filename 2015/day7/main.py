lines = open(0).read().strip().splitlines()

wires = dict()
a = 0

for line in lines:
    inst, var = line.split(' -> ')
    inst = inst.replace('OR', '|').replace('AND', '&').replace('LSHIFT', '<<').replace('RSHIFT', '>>').replace('NOT', '~')
    #print(f"{var}={inst}")
    #exec eller eval(f"wires[{var}] = {inst}")
print(a)