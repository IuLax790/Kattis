n = int(input())

for _ in range(n):
    a,b = input().split()
    a = int(a)
    dec = ""
    for char in b:
        char = int(char)
        sum = (a+char)%10
        dec+=str(sum)
    print(dec)
