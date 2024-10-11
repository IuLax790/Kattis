limits = list(zip("ABCDE",map(int,input().split()))) + [("F",0)]
print(limits)
score = int(input())
print(next(letter for letter,grade in limits if score>=grade))
