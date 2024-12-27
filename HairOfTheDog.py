hangover = 0
n = int(input().strip())
#read the sequence of days
days = [input().strip() for _ in range(n)]

# Traverse the days to count hangover days
for i in range(1,n):
    if days[i-1]=="drunk" and days[i]=="sober":
        hangover+=1
print(hangover)
