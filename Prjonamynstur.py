
inp = input().split()
count = 0
m, n = int(inp[0]), int(inp[1])
for i in range(m):
    i = input()
    for j in i:
        if j==".":
            count += 20
        if j=="O":
            count += 10
        if j=="/" :
            count += 25

        if j=="A":
            count += 35
        if j=="^":
            count += 5
        if j=="v":
            count += 22
        else:
            count+=25
    print(count)
