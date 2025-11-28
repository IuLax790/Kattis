a = 0
b = 0
s = int(input())
if s>0 and s!=1:
    a = 1
    b = s-1
elif s<0 and s!=-1:
    a = -1
    b = s+1
elif s<0 and s==-1:
    a = -2
    b = 1
elif s>0 and s==1:
    a = -1
    b = 2
elif s==0:
    a= -999
    b = 999
print(a,b, sep=' ')
    
