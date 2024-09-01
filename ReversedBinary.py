number = int(input())
reversedBinaryNumber = f'{number:0b}'[::-1]
reversedBinaryNumber = int(reversedBinaryNumber,2)
print(reversedBinaryNumber)
