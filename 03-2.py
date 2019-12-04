#!/usr/bin/env python

import input_day_three

def generateGrid(wires):
    grid = []
    horizontal_length = findMaxLength(wires) + 2
    vertical_length = findMaxHeight(wires) + 2

    for i in range(horizontal_length):
        grid.append(['.'] * vertical_length)

    return grid

def findMaxLength(wires):
    max = 0
    for i in wires[0]:
        if i[0] == 'L' or i[0] == 'R':
            if int(i[1]) > max:
                max = int(i[1])
    for i in wires[1]:
        if i[0] == 'L' or i[0] == 'R':
            if int(i[1]) > max:
                max = int(i[1])
    return max

def findMaxHeight(wires):
    max = 0
    for i in wires[0]:
        if i[0] == 'U' or i[0] == 'D':
            if int(i[1]) > max:
                max = int(i[1])
    for i in wires[1]:
        if i[0] == 'U' or i[0] == 'D':
            if int(i[1]) > max:
                max = int(i[1])
    return max

def parseInput(input):
    input = input.split('\n')
    input[0] = input[0].split(',')
    input[1] = input[1].split(',')
    return input

def calculateWiresTurns(wires):
    wire0 = [ 0, 0 ]
    wire1 = [ 0, 0 ]
    wire0_positions = []
    wire1_positions = []

    for i in wires[0]:
        if i[0] == 'U':
            wire0[0] += int(i[1:])
            wire0_positions.append(wire0.copy())
        elif i[0] == 'D':
            wire0[0] -= int(i[1:])
            wire0_positions.append(wire0.copy())
        elif i[0] == 'L':
            wire0[1] -= int(i[1:])
            wire0_positions.append(wire0.copy())
        elif i[0] == 'R':
            wire0[1] += int(i[1:])
            wire0_positions.append(wire0.copy())
    for i in wires[1]:
        if i[0] == 'U':
            wire1[0] += int(i[1:])
            wire1_positions.append(wire1.copy())
        elif i[0] == 'D':
            wire1[0] -= int(i[1:])
            wire1_positions.append(wire1.copy())
        elif i[0] == 'L':
            wire1[1] -= int(i[1:])
            wire1_positions.append(wire1.copy())
        elif i[0] == 'R':
            wire1[1] += int(i[1:])
            wire1_positions.append(wire1.copy())
    return wire0_positions, wire1_positions

def calculateWiresPaths(wires):
    wire0 = [ 0, 0 ]
    wire0_positions = []
    wire1 = [ 0, 0 ]
    wire1_positions = []
    wire_crossings = []

    for i in wires[0]:
        if i[0] == 'U':
            for j in range(int(i[1:])):
                wire0[0] += 1
                wire0_positions.append(wire0.copy())
        elif i[0] == 'D':
            for j in range(int(i[1:])):
                wire0[0] -= 1
                wire0_positions.append(wire0.copy())
        elif i[0] == 'L':
            for j in range(int(i[1:])):
                wire0[1] -= 1
                wire0_positions.append(wire0.copy())
        elif i[0] == 'R':
            for j in range(int(i[1:])):
                wire0[1] += 1
                wire0_positions.append(wire0.copy())
    for i in wires[1]:
        if i[0] == 'U':
            for j in range(int(i[1:])):
                wire1[0] += 1
                wire1_positions.append(wire1.copy())
                if wire1.copy() in wire0_positions:
                    wire_crossings.append(wire1.copy())
        elif i[0] == 'D':
            for j in range(int(i[1:])):
                wire1[0] -= 1
                wire1_positions.append(wire1.copy())
                if wire1.copy() in wire0_positions:
                    wire_crossings.append(wire1.copy())
        elif i[0] == 'L':
            for j in range(int(i[1:])):
                wire1[1] -= 1
                wire1_positions.append(wire1.copy())
                if wire1.copy() in wire0_positions:
                    wire_crossings.append(wire1.copy())
        elif i[0] == 'R':
            for j in range(int(i[1:])):
                wire1[1] += 1
                wire1_positions.append(wire1.copy())
                if wire1.copy() in wire0_positions:
                    wire_crossings.append(wire1.copy())
    return wire0_positions, wire1_positions, wire_crossings

def calculateWiresCrossings(wire0, wire1):
    crossings = []
    for i in wire0:
        if i in wire1:
            crossings.append(i.copy())
    return crossings

def findShortestDistance(crossings):
    result = [ 10000000000, [0,0] ]
    for i in crossings:
        pos1 = abs(i[0])
        pos2 = abs(i[1])
        manhattan = pos1 + pos2
        if manhattan < result[0]:
            result[0] = manhattan
            result[1] = i
#    result = min([sum(i) for i in crossings])
    return result

def findFewestJumps(crossings, wire0, wire1):
    jumps = []
    for i in crossings:
        jumps.append(wire0.index(i) + wire1.index(i) + 2)
    return min(jumps)

if __name__ == "__main__":
    wires = parseInput(input_day_three.input)
    wire0, wire1, crossings = calculateWiresPaths(wires)
    answer = findFewestJumps(crossings, wire0, wire1)
    print(answer)
