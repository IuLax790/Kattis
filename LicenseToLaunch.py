n = int(input())
amountOfSpaceJunk = list(map(lambda spaceJunk : int(spaceJunk),input().split()))

bestDayOfLaunch = amountOfSpaceJunk.index(min(amountOfSpaceJunk))
print(bestDayOfLaunch)
