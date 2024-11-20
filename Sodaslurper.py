inp = input().split()
numberOfOwnedEmptyBottles ,numberOfFoundEmptyBottles ,numberOfRequiredEmptyBottles  = int(inp[0]),int(inp[1]),int(inp[2])

totalBottles = 0
numberOfEmptyBottles = numberOfOwnedEmptyBottles + numberOfFoundEmptyBottles
while numberOfRequiredEmptyBottles <= numberOfEmptyBottles:
    leftover = numberOfEmptyBottles % numberOfRequiredEmptyBottles
    newBottles = numberOfEmptyBottles // numberOfRequiredEmptyBottles
    totalBottles += newBottles
    numberOfEmptyBottles = leftover + newBottles

print(totalBottles)
