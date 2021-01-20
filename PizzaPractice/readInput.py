#!/usr/bin/env python3
import itertools
inputFile = open("input.txt","r")
firstLine = inputFile.readline()
firstLine=firstLine.rstrip()
pizza_dict =[]
if len(firstLine) > 0 :
    totalPizza = firstLine[0]
    groupTwo =firstLine[1]
    groupThree =firstLine[2]
    groupFour =firstLine[3]
    for line in itertools.islice(inputFile, 0, int(totalPizza)):
        pizza_dict.append(line[0])
        pizza_dict.append(line[1:])
  
print(pizza_dict)   
   

