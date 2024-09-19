word = ""
inp = input().split()
rows = int(inp[0])
columns = int(inp[1])
for i in range(rows):
    i = input()
    i = i.replace(".","")
    word +=i
print(word)
