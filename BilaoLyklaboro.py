line = input()
for count, word in enumerate(line):
    print(word if count == 0 else word if line[count-1] != word else '', end='')
