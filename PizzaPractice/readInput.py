#!/usr/bin/env python3
import math
def readInput():
    pizzaDetails = []
    pizzaTotal, groupOne,groupTwo,groupThree = map(int,input().split())
    for value  in range(0,pizzaTotal):
            pizzaDetails.append(input())
    return( pizzaTotal,groupOne,groupTwo,groupThree,pizzaDetails)

def selectTeam(processInput):
    groupList = []
    pizzaTotal = processInput[0]
    groupList = list(processInput[1:])
    print(groupList)
    groupOneTotalMember = groupList[0] * 2
    groupTwoTotalMember = groupList[1]* 3
    groupThreeTotalMember = groupList[2] * 4

    if(pizzaTotal>=(groupOneTotalMember+groupTwoTotalMember+groupThreeTotalMember)):
            return(groupList)
    else:
         if(pizzaTotal>9):
             allTeamSet = math.floor(pizzaTotal/9)
             excessPizza = pizzaTotal%9
             if(allTeamSet <=min (groupList)):

                 groupList = [x - allTeamSet for x in groupList]
                 calculateLess(excessPizza,groupList)
             else:
                difference = allTeamSet - min(groupList)
                allTeamSet = allTeamSet -difference
                excessPizza = excessPizza + (difference*9)
                groupList = [x - allTeamSet for x in groupList]
                positionToChange = groupList.index(min(groupList))
                groupList.remove(groupList[positionToChange])
                groupList.insert(positionToChange,0)
                print(groupList)
                calculateLess(pizzaTotal, groupList)


      else:
            calculateLess(pizzaTotal, groupList)

def calculateLess(pizzaTotal, groupList):
    remainPizzaList = []
    

    while(pizzaTotal>2 and member<=4):
            pizzaTotal = pizzaTotal-member
            remainPizzaList.append(member)
            member = member+1

    print(remainPizzaList)
        
        
            
   
if __name__ == "__main__":
    processInput = readInput()
    selectTeam(processInput[0:4])

