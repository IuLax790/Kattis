l = []
m = []
rest = 0
n = int(input())
for i in range(n):
    i = input()
    l.append(i)
for j in l:
   
    if j[1:3]=="39":
        j = j[3:]
        m.append(j)
for j in m:
    if len(j)==9 or len(j)==10:
        rest+=1
print(rest)
