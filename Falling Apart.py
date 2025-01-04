Alice = 0
Bob = 0
n = int(input())
i = list(map(int,input().split()))
i.sort(reverse=True)
for j in range(len(i)):
    if j%2==0:
        Alice+=i[j]
    else:
        Bob+=i[j]
print(Alice,Bob)
    
