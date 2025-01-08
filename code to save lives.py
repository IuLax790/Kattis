results = []
for _ in range(int(input())):
    num1 = int("".join(input().split()))
    num2 = int("".join(input().split()))
    results.append(num1+num2)
    
for result in results:
    print(" ".join(str(result)))
