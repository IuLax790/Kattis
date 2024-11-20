inp = input().split()
n,s = int(inp[0]),int(inp[1])
for i in range(n):
    i = input().split()
    l,u = int(i[0]),int(i[1])
    if l<=s<=u:
        s+=1
print(s)
