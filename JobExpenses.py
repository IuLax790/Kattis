n = int(input())
expenses = 0
i = list(map(int,input().split()))

for j in i:
    if j<0:
        expenses+=j
print(abs(expenses))
