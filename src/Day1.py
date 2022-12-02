#!/usr/bin/python3

givenFile = open('../resources/Day1input.txt', 'r')
currentElfCals = 0
elves = []
for line in givenFile:
    if line.strip():
        currentElfCals += int(line.strip())
    else:
        elves.append(currentElfCals)
        currentElfCals = 0

elves.sort(reverse=True)
print(elves[0])
print(sum(elves[:3]))
