#!/usr/bin/python3

inputFile = open('../resources/Day1Input', 'r')
currentElfCals = 0
elves = []
for line in inputFile:
    if line.strip():
        currentElfCals += int(line.strip())
    else:
        elves.append(currentElfCals)
        currentElfCals = 0

elves.sort(reverse=True)
print(elves[0])
print(sum(elves[:3]))
