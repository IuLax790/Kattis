inp = input().split()
a,b = int(inp[0]),int(inp[1])
num1 = b-a
num2 = a-b
if a<b and 0<=num1<=1:
    print("Dr. Chaz will have", num1 ,"piece of chicken left over!")
elif a<b and num1>1:
    print("Dr. Chaz will have", num1 ,"pieces of chicken left over!")
elif b<a and 0<=num2<=1:
    print("Dr. Chaz needs", num2 ,"more piece of chicken!")
if b<a and num2>1:
    print("Dr. Chaz needs", num2 ,"more pieces of chicken!")
