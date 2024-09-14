a,b = list(map(int,input().split(' ')))

if (a==0) and (b==0):
    print("Not a moose")
elif a>b:
    print("Odd",a*2)
elif b>a:
    print("Odd",b*2)
elif (a==b):
    print("Even",(a*2))
