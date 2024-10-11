n = input().split("/")
a,b,c = int(n[0]),int(n[1]),int(n[2])
if b>12 and a<b:
    print("US")
elif a<13 and b<13:
    print("either")
else:
    print("EU")
