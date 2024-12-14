while True:
    line = input().strip()
    if line == "0 0":
        break
    
    numerator,denominator = map(int,line.split())
    whole_number = numerator//denominator
    remainder = numerator%denominator
    print(whole_number,remainder,"/",denominator)
