#!/usr/bin/python3
import csv
import string

moves = list()
part1Score = 0
part2Score = 0

with open('../resources/Day2Input', 'r') as inputFile:
    strategyReader = csv.reader(inputFile, delimiter=' ')
    for row in strategyReader:
        currScore = 0
        opponent = string.ascii_uppercase.index(row[0]) + 1
        player = string.ascii_uppercase.index(row[1]) - 22

        # Part1
        part1Score += player
        if opponent == player:
            part1Score += 3
        elif (opponent - player) % 3 == 2:
            part1Score += 6

        # Part2
        if player == 1:
            part2Score += 0
            part2Score += (opponent + 2) % 3 if opponent + 2 > 3 else opponent + 2
        elif player == 2:
            part2Score += 3
            part2Score += opponent
        elif player == 3:
            part2Score += 6
            part2Score += (opponent + 1) % 3 if opponent + 1 > 3 else opponent + 1

print(f'Part1: {part1Score}')
print(f'Part2: {part2Score}')
