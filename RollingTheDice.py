res1 = 0
res2 = 0
s = input()
s= s.replace("d",",")
s = s.replace("+",",")
s = s.split(",")
s[0] = int(s[0]) ;s[1] = int(s[1]) ; s[2] = int(s[2])
res1 +=(s[0] + s[2])
res2+=(s[0]*s[1]) + s[2]
print((res1+res2)/2)
    
