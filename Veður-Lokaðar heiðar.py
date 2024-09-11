v = int(input())
n = int(input())
for i in range(n):
    inp = input().split()
    x,y = inp[0],int(inp[1])
    if y<v:
        print(x,"lokud",sep=" ")
    else:
        print(x,"opin",sep=" ")
