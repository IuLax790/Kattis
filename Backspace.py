result = []
s = input()
for char in s:
    if char=='<':
        if result:
            result.pop()
    else:
        result.append(char)
print(''.join(result))
