#!/usr/bin/env python3
import itertools
import sys
inpt = sys.stdin.read().splitlines()
firstLine = inpt[0]
pizza_list = []
if firstLine :
    pizzaTotal, grpOne, grpTwo, grpThree = firstLine.split()    
for line in itertools.islice(inpt, 1, int(pizzaTotal)) :
    pizza_list.append(line.strip())
