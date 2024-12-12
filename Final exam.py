n = int(input().strip())
correct_answers = [input().strip() for _ in range(n)]
score = 0

for i in range(1,n):
    if correct_answers[i]==correct_answers[i-1]:
        score+=1
print(score)
