data = input().split()
die1 = int(data[0])
die2 = int(data[1])

#we'll find out between minimum and maximum , what is the most probable sum of values
minimum = min(die1,die2)
maximum = max(die1,die2)

for value in range(minimum+1, maximum+2):
    print(value)
