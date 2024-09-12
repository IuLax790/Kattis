cards = input()
pairs = []
for i in range(0,len(cards),3):
    pairs.append(cards[i:i+3])

if len(pairs) != len(set(pairs)):
    print("GRESKA")
else:
    p = 13 - cards.count("P")
    k = 13 - cards.count("K")
    h = 13 - cards.count("H")
    t = 13 - cards.count("T")
    print(p,k,h,t)
