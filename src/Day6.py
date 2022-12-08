#!/usr/bin/python3

signal = open('../resources/PuzzleInputs/Day6Input', 'r').read()

# Part 1
firstMarker = 0
for marker in enumerate(range(1, len(signal))):
    print(signal[marker[1]-4:marker[1]])
    if len(set(signal[marker[1]-4:marker[1]])) == 4:
        firstMarker = marker[1]
        break

print(f'First Marker: {firstMarker}')

# Part 2
longMarker = 0
for marker in enumerate(range(1, len(signal))):
    print(signal[marker[1]-14:marker[1]])
    if len(set(signal[marker[1]-14:marker[1]])) == 14:
        longMarker = marker[1]
        break

print(f'Long Marker: {longMarker}')
