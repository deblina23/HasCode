#!/usr/bin/env python3
import itertools
def print_input(processInput):
    pizzaTotal,grpOne,grpTwo,grpThree,pizzaList = tuple(value for value in processInput)
    print(pizzaTotal,grpOne,grpTwo,grpThree,pizzaList)  

def read_input():
    lines = []
    while True:
        line = input()
        if ("" == line):
            break
    lines.append(line)
    return lines

def process_input(inputLines):
    pizzaList = []
    firstLine = inputLines[0]
    if firstLine :
        pizzaTotal, grpOne, grpTwo, grpThree = [int(n) for n in firstLine.split()]
    for anotherLines in itertools.islice(inputLines, 1, int(pizzaTotal)) :
            pizzaList.append(anotherLines.strip())
    return(pizzaTotal,grpOne,grpTwo,grpThree,pizzaList)       

if __name__ == "__main__":
    inputLines=read_input()
    processInput = process_input(inputLines)
    print_input(processInput)
