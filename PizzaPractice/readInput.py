#!/usr/bin/env python3
import itertools
from itertools import combinations

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

def findPairs(lst, K, total):      
    res = [] 
    for i in range(total, 0, -1):
        for var in combinations(lst, i):
            if sum(var) == K:
                if var not in res:
                    res.append(var)
    return res 
def create_list(rangeList):
    val=[2,3,4]
    lst = []   
    pos = 0
    while(pos<3):
        x = 0
        while(x<rangeList[pos]):
            lst.append(val[pos])
            x = x + 1
        pos = pos + 1
    print("The fina list"+str(lst))
    return lst

if __name__ == "__main__":
    
    inputLines=read_input()
    processInput = process_input(inputLines)
    print_input(processInput)
    totalList = create_list(list(processInput[1:4]))
    totalTeam = (sum(processInput[1:4]))
    print("The final pairs are")
    print(findPairs(totalList,processInput[0],totalTeam))
    
