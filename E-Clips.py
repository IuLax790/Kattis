s = input().split()
l = []
for i in s:
    if "e"  in i:
        l.append(i)

print(" ".join(l) if len(l)>0 else "oh noes")
