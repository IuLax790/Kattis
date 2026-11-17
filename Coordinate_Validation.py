n = int(input())
for i in range(n):
    i = input().split()
    a = float(i[0]);b=float(i[1])
    if -180<=a<=180 and -90<=b<=90:
        print("VALID")
    else:
        print("INVALID")
