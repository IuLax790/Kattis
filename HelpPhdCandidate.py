n = int(input())
for _ in range(n):
    i = input()
    if(i=='P=NP'):
        print("skipped")
    else:
        i = i.split('+')
        print(int(i[0])+int(i[1]))
