x,y,z = input().split()
x = int(x);y=int(y);z=int(z)
average = (x*0.25 + y*0.25 + z*0.5)

if 0<average<60:
    print("F")
elif 60<=average<70:
    print("D")
elif 70<=average<80:
    print("C")
elif 80<=average<90:
    print("B")
elif 90<=average<100:
    print("A")
    
    
    
