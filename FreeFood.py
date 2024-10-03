n= int(input())
st = set()
for _ in range(n):

    i = input().split()
    a,b = int(i[0]),int(i[1])
    for i in range(a,b+1):

        st.add(i)
print(len(st))
