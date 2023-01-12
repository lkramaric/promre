from typing import DefaultDict

# Input Matrix
tsp = [[-1, 100, 152, 300, 421], [100, -1, 192, 214, 98], [152, 192, -1, 99, 156], [300, 214, 99, -1, 145], [421, 98, 156, 145, -1]]
sum = 0
counter = 0
i = 0
j = 0
#putanja
route = []
min = 9999999
#lista obavljenih lokacija
visitedLocaton = DefaultDict(int)
visitedLocaton[0] = 1
for k in range (0, len(tsp)):
    route.append(0)

#pohlepni algoritam
#do kraja matrice
while (i < len(tsp) and j < len(tsp[i])):
    if (counter >= len(tsp[i]) - 1):
        break
    if (visitedLocaton[j] != 1):
        if(tsp[i][j] < min and tsp[i][j] != -1):
            min = tsp[i][j]
            route[counter] = j + 1
    j = j + 1

    
    if (j == len(tsp[i])):
        sum = sum + min
        min = 9999999
        visitedLocaton[route[counter] - 1] = 1
        j = 0
        i = route[counter] - 1
        counter = counter + 1

#povratak u početnu lokaciju
route[counter] = 1
min = tsp[i][0]

sum = sum + min
print("Minimum cost is: ", sum)
print("Route is: ", route)
 


