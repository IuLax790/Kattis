data = input().split()
month = data[0].upper()
day = int(data[1])
if month == "OCT" and day == 31 or month == "DEC" and day == 25:
    print("yup")
else:
    print("nope")
