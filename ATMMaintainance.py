result = []
m,k = input().split()
m = int(m) ; k = int(k)
n = list(map(int,input().split()))
balance = k
for i in n:
    if balance>=i:
        balance-=i
        result.append("1")
    else:
        result.append("0")
print("".join(result))
