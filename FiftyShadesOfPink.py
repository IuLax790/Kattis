n = int(input())
count = 0
for _ in range(n):
    i = input()
    i = i.lower()
    if "pink" in i or "rose" in i:
        count+=1

print(count if count>0 else "I must watch Star Wars with my daughter")
