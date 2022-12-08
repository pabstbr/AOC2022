#!/usr/bin/python3
import copy
import re
from collections import deque

crateState, moves = open('../resources/PuzzleInputs/Day5Input', 'r').read().split('\n\n')
stacks = []

for line in crateState.splitlines()[:-1]:
    print(line)
    for stackNum, crateValPos in enumerate(range(1, len(line), 4)):
        while stackNum >= len(stacks):
            stacks.append(deque())
        if line[crateValPos] != ' ':
            stacks[stackNum].append(line[crateValPos])

# I hate references a bit right now
stacksDupe = copy.deepcopy(stacks)

for move in moves.splitlines():
    numMoved, fromStack, toStack = map(int, re.findall(r"\d+", move))

    # Part 1
    for crate in range(numMoved):
        stacks[toStack - 1].appendleft(stacks[fromStack - 1].popleft())

    # Part 2
    craneHolding = deque()
    print(stacksDupe)
    for crate in range(numMoved):
        craneHolding.appendleft(stacksDupe[fromStack - 1].popleft())
    stacksDupe[toStack - 1].extendleft(craneHolding)

print(f'Part 1: {"".join(x[0] for x in stacks)}')
print(f'Part 2: {"".join(x[0] for x in stacksDupe)}')
