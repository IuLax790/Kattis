n = int(input())
for _ in range(n):
    a,b,c = input().split()
    a = int(a);b = int(b);c = int(c)

    if (a+b)==c or (a-b)==c or (b-a)==c or (b/a)==c or (a/b)==c or (b+a)==c or (b*a)==c:
        print("Possible")
    else:
        print("Impossible")
