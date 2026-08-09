s = input().split()
while int(s[0])!=int(s[1]):
    if int(s[0])>int(s[1]):
        print("More")
        s = input().split()
    if int(s[1])>int(s[0]):
        print("Less")
        s = input().split()
else:
    print("")
    
