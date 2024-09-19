l = [input() for _ in range(5)]
fbi_blimps_indexes = []
for i in range(len(l)):
    if "FBI" in l[i]:
        fbi_blimps_indexes.append(str(i+1))
if fbi_blimps_indexes:
    print(" ".join(fbi_blimps_indexes))
else:
    print("HE GOT AWAY!")
