n = int(input())
wins=0
for i in range(n):
    i = input()
    if "CD" not in i:
        wins+=1
print(wins)
