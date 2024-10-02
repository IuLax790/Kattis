from datetime import date
inp = input().split()
d,m = int(inp[0]),int(inp[1])
givenDate = date(2009,d,m)
weekDay = givenDate.strftime("%A")
print(weekDay)
