#!/usr/bin/env python3
import itertools
inputFile = input("Enter the File:")
inputFile = open(inputFile,"r")
firstLine = inputFile.readline()
pizza_list = []
if firstLine:
    pizzaTotal, grpOne, grpTwo, grpThree = firstLine.split(" ")
    
for line in itertools.islice(inputFile, 0, int(firstLine[0])):
    pizza_list.append(line.strip())
   

