import tsplib95
import random
import math
import copy
import time
import random
from random import randint
import numpy as np
import matplotlib.pyplot as plt
from typing import DefaultDict

data = tsplib95.load("/home/luka/Desktop/Stari/tsplib95-0.7.1/tsplib95-0.7.1/tests/data/att532.tsp")
cities = list(data.get_nodes())
print(cities)

def closestNeighbour(initialSolution):
    i= 0
    j = 0
    sum = 0
    cnt = 0
    print("uso")
    min = 99999999
    closestSolution = []
    visitedLocation = DefaultDict(int)
    visitedLocation[0] = 1
    for k in range(0, 532):
        closestSolution.append(0)

    while(i < 532 and j < 532):
        #if(i == 522):
        #    print(closestSolution)
        #    break
        if(cnt >= 531):
            break
        if(visitedLocation[j] != 1):
            #print("i je = ", i, "j je = ", j)
            if(data.get_weight(i+1, j+1) < min and data.get_weight(i+1, j+1) != 0):
                min = data.get_weight(i+1, j+1)
                closestSolution[cnt] = j + 1
        j = j + 1

        if(j == 532):
            sum = sum + min
            #print("dodana udaljenost je: ", min)
            min = 9999999
            #print("cnt je : ", cnt)
            #print("DULJINA JE: ", len(closestSolution))
            visitedLocation[closestSolution[cnt] - 1] = 1
            j = 0
            i = closestSolution[cnt] - 1
            cnt = cnt + 1
    closestSolution[cnt] = 1
    min = data.get_weight(i, 1)
    sum = sum + min
    print("minimalna nakon greedy je: ", sum)
    for i in range(0, len(closestSolution)):
        closestSolution[i] = closestSolution[i]
    print(closestSolution)
    print(len(closestSolution))
    return closestSolution


def invertRoute(currentSolution):
    newSolution = []
    #create only one candidate solution, it is possible to create more and pick a random one
    for i in range(1):
        city1 = 0
        city2 = 0
        while (city1 == city2):
            city1 = randint(1, len(currentSolution))
            city2 = randint(1, len(currentSolution))
        if (city2 < city1):
            c = city1
            city1 = city2
            city2 = c
        temp = currentSolution[city1:city2]
        tempSolution = currentSolution[:city1] + temp[::-1] + currentSolution[city2:]
        for j in range(len(tempSolution)):
            newSolution.append(tempSolution[j])
    return newSolution

def swapCities(currentSolution):
    newSolution = currentSolution.copy()
    city1 = 0
    city2 = 0
    while (city1 == city2):
        city1 = randint(1, len(currentSolution))
        city2 = randint(1, len(currentSolution))
    newSolution[city1-1], newSolution[city2-1] = newSolution[city2-1], newSolution[city1-1]
    return newSolution

def generateNew(currentSolution, x):
    x = random.choice([0, 1])
    if (x == 0 or True):
        return invertRoute(currentSolution)
    return swapCities(currentSolution)

def calculateCost(solution):
    totalDistance = 0
    for i in range (len(solution) - 1):
        city1 = solution[i] 
        city2 = solution[i+1]
        distance = data.get_weight(city1, city2)
        #print(data.get_weight(city1, city2))
        totalDistance += distance
    city1 = solution[len(solution) - 1]
    city2 = solution[0]
    distance = data.get_weight(city1, city2)
    totalDistance += distance
    return totalDistance

startTemp = 5000
alpha = 0.99

currentTemp = startTemp
currentSolution = cities
#option of closest neighbour or 1-2-3-4-5-6 and so on
currentSolution = closestNeighbour(currentSolution)
currentCost = calculateCost(currentSolution)
print("current cost is: ", currentCost)
counter = 0
counter2 = 0
start = time.time()
brAcc = 0
brUk = 0
brNon = 0
#create new solutions until it repeats itself multiple times
while (counter < 3000 and counter2 < 20000):
    #print("radim ", counter)
    #print("ponavljam", counter2)   
    x = 0
    x = 1
    #x = 2
    newSolution = generateNew(currentSolution, x)
    #print(newSolution)
    newCost = calculateCost(newSolution)
    #print("new cost is: ", newCost)
    #check wheter new solution is better
    if (newCost < currentCost):
        currentSolution = newSolution
        currentCost = newCost
        counter = 0
        counter2 = 0
        brUk = brUk + 1
        #print("novo je bolje")
        #print("new cost is: ", newCost)
    elif (newCost == currentCost):
        currentSolution = newSolution
        counter = 0
        counter2 = counter2 + 1
        brUk = brUk + 1
    else:
        #print("test nakon vjerojatnosti")
        #small chance to accept worse solutions
        costDiff = 1/float(newCost) - 1/float(currentCost)
        if (random.uniform(0, 1) < math.exp((currentCost - newCost) / float(currentTemp))):
            brAcc = brAcc + 1
            currentSolution = newSolution
            currentCost = newCost
            counter = 0
            counter2 = 0
            #print("novo nije bolje al eto")
        #same solution repeated itself
        else:
            counter = counter + 1   
            #print("novo nije bolje")
            brNon = brNon + 1
    currentTemp = currentTemp * alpha
time_elapsed = time.time() - start
print("prošlo vrijeme je ", time_elapsed)
print("konačno rješenje je :", currentSolution)
print("konačna cijena je: ", currentCost)    
print("promjena2")  
print(brUk, " je ukupni broj prihvacenih")
print(brAcc, " je ukupan broj krivo prihvacenih")
print(brNon, " je ukupan broj odbijenih")


