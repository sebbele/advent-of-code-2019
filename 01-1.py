#!/usr/bin/env python

import input_day_one

def fuelReq(mass):
    fuel = ( mass // 3 ) - 2
    return fuel

result = []

for i in input_day_one.input:
    result.append(fuelReq(i))

print(sum(result))
