#!/usr/bin/env python3
import math
import itertools

def fetch_input():
    inputFile = open("e_many_teams.in", "r")
    firstLine = inputFile.readline()
    pizza_list = []
    if firstLine:
        pizzaTotal, grpOne, grpTwo,grpThree = map(int,firstLine.split())
    for line in itertools.islice(inputFile, 0, int(pizzaTotal)):
        pizza_list.append(line.strip())
    return (pizzaTotal, grpOne, grpTwo, grpThree, pizza_list)

def frequency_input(totalPizza, pizzaTypes):
    ingredientMap = {}
    for pizzaType in pizzaTypes:
        for ingredient in pizzaType.split(' ')[1:]:
                ingredientMap[ingredient] = ingredientMap.get(ingredient, 0) + 1
    pizzaPriorty = []
    for index, pizzaType in enumerate(pizzaTypes):
        ingredients = pizzaType.split(' ')[1:]
        result = 1
        for ingredient in ingredients:
            result = result * (ingredientMap.get(ingredient)/totalPizza)
        pizzaPriorty.append((str(index), result, ingredients))

    pizzaPriorty = sorted(pizzaPriorty,key=lambda x: x[1])
    return(pizzaPriorty)

def selectTeam(processInput):
    pizzaTotal = processInput[0]
    total = 0
    totalListCount = [0, 0, 0,0]
    groupList = list(processInput[1:])
    memberList = [2, 3, 4]
    for ele in range(0, len(groupList)):
        total = total + (groupList[ele]*memberList[ele])
    if(pizzaTotal-total>=0):
        for ele in range(0, len(groupList)):
            totalListCount[memberList[ele]-1]= groupList[ele]
            totalTeamCount = totalTeamCount + groupList[ele]
    else:
        while True:
            resultSet = calculateTeam(pizzaTotal, groupList, memberList)
            allTeamSetInitial, pizzaTotal, groupList, resultList = tuple(value for value in resultSet)
            for pos in range(4):
                totalListCount[pos] = totalListCount[pos] + resultList[pos]
            if (pizzaTotal < 2):
                break
            for value in groupList:
                if(value<=0):
                    zeroposition=groupList.index(value)
                    groupList.remove(value)
                    memberList.remove(memberList[zeroposition])

    totalListCount.remove(totalListCount[0])
    return(totalListCount)

def calculateTeam(pizzaTotal, groupList, memberList):
    currentMembers = sum(memberList)
    resultList = [0]* 4
    minimumValue = 0
    difference = 0
    flag = False
    if (pizzaTotal >= currentMembers):

        allTeamSet = math.floor(pizzaTotal / currentMembers)
        excessPizza = pizzaTotal % currentMembers
        if (allTeamSet > min(groupList)):
            minimumValue = min(groupList)
            difference = allTeamSet - min(groupList)
            flag = True

        for pos in range(len(groupList)):
            if (flag):
                resultList[memberList[pos] - 1] = minimumValue
                if(groupList[pos]==minimumValue):
                    pass
                else:
                    excessPizza = excessPizza + (abs(difference) * memberList[pos])

                groupList[pos] = groupList[pos] - minimumValue
                allTeamSet = minimumValue

            else:
                resultList[memberList[pos] - 1] = allTeamSet
                groupList[pos] = groupList[pos]- allTeamSet


        return (allTeamSet, excessPizza, groupList, resultList)
    else:
        return (calculateLessItem(pizzaTotal, groupList, memberList))


def calculateLessItem(pizzaTotal, groupList, memberList):
    resultList = [0]* 4
    TeamCount = 0
    for memberPos in range(len(memberList)):
        if (pizzaTotal > 0):
            pizzaTotal = pizzaTotal - memberList[memberPos]
            resultList[memberList[memberPos]- 1] = resultList[memberList[memberPos]- 1] + 1
            TeamCount = TeamCount + 1
            groupList[memberPos] = groupList[memberPos] - 1

    return (TeamCount, pizzaTotal, groupList, resultList)

def result(processSelection,processPriority):
    twoMembers,threeMembers,fourMembers = tuple(value for value in processSelection[1])
    pointer = 0
    listFinal = []

    for _ in range(fourMembers):
        listFinal.append(('4',processPriority[pointer][0],processPriority[pointer+1][0],processPriority[pointer+2][0],processPriority[pointer+3][0]))
        pointer= pointer + 4
    for _ in range(threeMembers):
        listFinal.append(('3',processPriority[pointer][0],processPriority[pointer+1][0],processPriority[pointer+2][0]))
        pointer= pointer + 3
    for _ in range(twoMembers):
        listFinal.append(('2', processPriority[pointer][0], processPriority[pointer + 1][0]))
        pointer = pointer + 2

    return listFinal
if __name__ == "__main__":
    processInput = fetch_input()
    processSelection = selectTeam(processInput[0:4])
    processPriority = frequency_input(int(processInput[0]),processInput[4])
    finalResult = result(processSelection,processPriority)
    outputFile = open("./output/e_many_teams.in", "w+")
    outputFile.write(str(len(finalResult))+"\n")
    for line in finalResult:
        outputFile.write(' '.join(line)+"\n")
    outputFile.close()