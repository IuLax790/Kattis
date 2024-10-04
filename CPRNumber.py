n = input()
n = n.replace("-","")
sum = 0
sum+=int(n[0])*4
sum+=int(n[1])*3
sum+=int(n[2])*2
sum+=int(n[3])*7
sum+=int(n[4])*6
sum+=int(n[5])*5
sum+=int(n[6])*4
sum+=int(n[7])*3
sum+=int(n[8])*2
sum+=int(n[9])*1
print(1 if sum%11==0 else 0)
