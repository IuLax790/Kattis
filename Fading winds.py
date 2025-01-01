h,k,v,s = map(int,input().split())
distance = 0
while h>0:
    v+=s
    v-=max(1,v//10)
    if v>=k:
        h+=1
    elif 0<v<k:
        h-=1
        if h==0:
            v=0
    elif v<=0:
        h=0
        v=0
    distance +=v
    if s>0:
        s-=1
print(distance)
