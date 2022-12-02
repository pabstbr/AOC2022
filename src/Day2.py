#!/usr/bin/python3
import csv
import string

moves = list()
score = 0
part2Score = 0

with open('../resources/Day2Input', 'r') as inputFile:
    strategyReader = csv.reader(inputFile, delimiter=' ')
    for row in strategyReader:
        currScore = 0
        opponent = string.ascii_uppercase.index(row[0]) + 1
        outcome = string.ascii_uppercase.index(row[1]) - 22
        score += outcome

        if outcome == 1:
            part2Score += 0
            part2Score += (opponent + 2) % 3 if opponent + 2 > 3 else opponent + 2
        elif outcome == 2:
            part2Score += 3
            part2Score += opponent
        elif outcome == 3:
            part2Score += 6
            part2Score += (opponent + 1) % 3 if opponent + 1 > 3 else opponent + 1

        if opponent == outcome:
            score += 3
        elif opponent - outcome == -1 or opponent - outcome == 2:
            score += 6

print(f'Part1: {score}')
print(f'Part2: {part2Score}')
