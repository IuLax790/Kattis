Arnar = 0
Hannes = 0
n = input()
for i in n:
    if i=="H":
        Hannes+=1
    if i=="A":
        Arnar+=1
if Hannes<Arnar:
    print("Hannes")
elif Arnar<Hannes:
    print("Arnar")
