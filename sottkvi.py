inp = input().split()
n,p,d = int(inp[0]),int(inp[1]),int(inp[2])
party = 0
for i in range(n):
    q = int(input())
    if (p+d)-q>=14:
        party+=1
  
print(party)
