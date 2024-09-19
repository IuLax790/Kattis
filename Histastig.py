n = int(input())
temp = []
for i in range(n):
    i = list(map(int,input().split()))
    print(max(i),min(i),sep=" ")
    break
