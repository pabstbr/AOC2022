#!/usr/bin/python3

with open('../resources/PuzzleInputs/Day4Input', 'r') as inputFile:
    containedRanges = 0
    overlappingRanges = 0

    for line in inputFile:
        pair1, pair2 = line.split(',')
        elf1Start, elf1End = pair1.split('-')
        elf2Start, elf2End = pair2.split('-')
        # not translating the stringified numbers to integers bit me in the ass for a _while_
        elf1Start, elf1End, elf2Start, elf2End = [int(location) for location in
                                                  [elf1Start, elf1End, elf2Start, elf2End]]
        # Part 1
        if elf1Start <= elf2Start and elf2End <= elf1End or elf2Start <= elf1Start and elf1End <= elf2End:
            containedRanges += 1

        # Part 2
        if not(elf1End < elf2Start or elf1Start > elf2End):
            overlappingRanges += 1

    print(f'Contained cleanup pairs: {containedRanges}')
    print(f'Overlapping cleanup pairs: {overlappingRanges}')
