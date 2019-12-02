#!/usr/bin/env python

import input_day_two

def opcodeCalc(position, input_list):
    pos1 = input_list[position]
    pos2 = input_list[position + 1]
    pos3 = input_list[position + 2]
    pos4 = input_list[position + 3]
    if pos1 == 1:
        res = input_list[pos2] + input_list[pos3]
    elif pos1 == 2:
        res = input_list[pos2] * input_list[pos3]
    elif pos1 == 99:
        return input_list[0]
    else:
        exit("[Function opcodeCalc] Invalid method {}. Position: {}".format(pos1, position))
    input_list[pos4] = res
    return input_list

def opcode(input_list):
    input_list = input_list
    for i in range(0, 10000, 4):
        input_list = opcodeCalc(i, input_list)
        if type(input_list) == int:
            break
    return input_list

if __name__ == "__main__":
    original_list = input_day_two.input.copy()
    input = input_day_two.input.copy()

    noun = 1
    verb = 1
    result = 0

    while result != 19690720:
        input = original_list.copy()
        verb+=1
        input[1] = noun
        input[2] = verb
        try:
            result = opcode(input)
        except IndexError:
            noun += 1
            verb = 0
        if result > 19690720:
            noun += 1
            verb = 0
    
    print(100 * noun + verb)
