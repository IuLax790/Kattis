inp = input().split()
x1,y1,x2,y2 = float(inp[0]),float(inp[1]),float(inp[2]),float(inp[3])
area = float((x2 - x1)*(y2-y1))
print(area if area>0 else area*-1)
