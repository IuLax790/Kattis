balance = []
for _ in range(int(input())):
    n = input()
    a = int(input())
    balance.append(a)
if sum(balance)>0:
    print("Usch, vinst")
elif sum(balance)<0:
    print("Nekad")
else:
    print("Lagom")
