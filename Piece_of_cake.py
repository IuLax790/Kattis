print((lambda n,h,v: max(h,n-h)*max(v,n-v)*4)(*map(int,input().split())))
