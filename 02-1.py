#!/usr/bin/env python

import input_day_two

def opcode(position, input_list):
    pos1 = input_list[position]
    pos2 = input_list[position + 1]
    pos3 = input_list[position + 2]
    pos4 = input_list[position + 3]
    if pos1 == 1:
        res = input_list[pos2] + input_list[pos3]
    elif pos1 == 2:
        res = input_list[pos2] * input_list[pos3]
    elif pos1 == 99:
        print(input_list[0])
        exit()
    else:
        exit("Invalid method {}. Position: {}".format(pos1, position))
    input_list[pos4] = res
    return input_list

if __name__ == "__main__":
    input = input_day_two.input
    input[1] = 12
    input[2] = 2
    for i in range(0, 1000, 4):
        input = opcode(i, input)
