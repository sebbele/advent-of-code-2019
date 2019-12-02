#!/usr/bin/env python

import input_day_one

def fuelReq(mass):
    fuel = ( mass // 3 ) - 2
    return fuel

def fuelTotal(mass):
    fuel_result = []
    fuel_result.append(fuelReq(mass))
    curr = fuel_result[0]
    while curr >= 0:
        curr = fuelReq(curr)
        if curr >= 0:
            fuel_result.append(curr)
    return sum(fuel_result)

result = []
for i in input_day_one.input:
    result.append(fuelTotal(i))

print(sum(result))
