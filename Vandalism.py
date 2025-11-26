letters = "UAPC"
n = input()
n = n.upper()
for i in n:
    if i in letters:
        letters = letters.replace(i,"")
print(letters)
