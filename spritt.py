inp = input().split()
n,x = int(inp[0]),int(inp[1])
bottles = 0
for i in range(n):
    i = int(input())
    bottles+=i
if x>=bottles:
    print("Jebb")
else:
    print("Neibb")
