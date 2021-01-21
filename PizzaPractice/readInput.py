#!/usr/bin/env python3
import itertools
inputFile = open("input.txt","r")
firstLine = inputFile.readline()
firstLine=firstLine.replace(" ","")
pizza_list =[]
if len(firstLine) > 0 :
    firstLine = tuple(firstLine.rstrip())
for line in itertools.islice(inputFile, 0, int(firstLine[0])):
    pizza_list.append(line.rstrip())
  
print(pizza_list)   
print(firstLine)
   

