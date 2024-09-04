import string
cust,ins = map(int,input().split())
customers,initials  = list(),list()

table = str.maketrans('','',string.ascii_lowercase + ' ')
for _ in range(cust):
    customers.append(input())
for _ in range(ins):
    inits,count,found  = input(),0, None
    for c in customers:
        if c.translate(table) == inits:
            count +=1
            found = c

    print(found) if count==1 else print("nobody") if count==0 else print("ambiguous")
