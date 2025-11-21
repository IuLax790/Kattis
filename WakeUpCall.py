input()
s1 = sum(map(int,input().split()))
s2 = sum(map(int,input().split()))
if s1>s2:
    print("Button 1")
elif s2>s1:
    print("Button 2")
else:
    print("Oh no")
