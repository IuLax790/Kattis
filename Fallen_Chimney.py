s = []
#number of lines
n = int(input())
#for each line
for i in range(n):
    #splitting each line into characters
    i = input().split()
    # first character is an int
    i[0] = int(i[0])
    # Bamse can make maximal noise only if the noise hasn't caused the chimney to fall off
    if i[1]=="nej":
        s.append(i[0])
print(max(s))
