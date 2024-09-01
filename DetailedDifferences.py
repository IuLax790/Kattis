
    
def test():
    text1 = input()
    text2 = input()
    differences = ""
    for letter1,letter2 in zip(text1,text2):
        if letter1 == letter2:
            differences += "."
        else:
            differences += "*"
    print(text1)
    print(text2)
    print(differences)
    print("")

numberOftest = int(input())
for _ in range(numberOftest):
    test()
