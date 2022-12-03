#!/usr/bin/python3
import string
from itertools import islice

with open('../resources/Day3Input', 'r') as inputFile:
    prioritySum = 0
    badgesSum = 0
    while True:
        next3Lines = list(islice(inputFile, 3))
        if not next3Lines:
            break
        # Part1
        for line in next3Lines:
            ruckOne, ruckTwo = line.strip()[:len(line.strip())//2], line.strip()[len(line.strip())//2:]
            commonItem = list(set(ruckOne).intersection(ruckTwo))[0]
            prioritySum += string.ascii_letters.index(commonItem) + 1
        # Part2
        commonBadge = list(set(next3Lines[0].strip()).intersection(next3Lines[1].strip()).intersection(next3Lines[2].strip()))[0]
        badgesSum += string.ascii_letters.index(commonBadge) + 1

    print(f'Priority Sum of duplicated items: {prioritySum}')
    print(f'Priority Sum of badges: {badgesSum}')