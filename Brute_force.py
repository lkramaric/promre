from itertools import permutations
tsp = [[-1, 100, 152, 300, 421], [100, -1, 192, 1, 98], [152, 192, -1, 99, 156], [300, 214, 99, -1, 145], [421, 98, 156, 145, -1]]
ways = list(permutations(range(1, len(tsp) + 1)))
#print(ways)
min = 999999
minRoute = []
i = 0
j = 0
x = 0
for way in ways:
    sum = 0
    for k in range (len(way)):
        if (k == len(way) - 1):
            i = way[k] - 1
            j = way[0] - 1
        else:
            i = way[k] - 1
            j = way[k + 1] - 1
        sum = sum + tsp[i][j]
    if (sum < min):
        min = sum
        minRoute = way

print("Minimum cost is: ", min)
print("Route is: ", minRoute)
