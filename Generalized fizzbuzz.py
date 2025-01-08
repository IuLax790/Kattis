fizz = 0
buzz = 0
fizzbuzz = 0
inp = input().split()
num,a,b =int(inp[0]),int(inp[1]),int(inp[2])
for i in range(1,num+1):
    if i%a==0 and i%b==0:
        fizzbuzz+=1
    elif i%a==0:
        fizz+=1
    elif i%b==0:
        buzz+=1
    
    
print(fizz,buzz,fizzbuzz)
