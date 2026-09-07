h,n = input().split()
h = int(h)
n = int(n)
standard,fire,ice,light = input().split()
standard = int(standard)
fire = int(fire)
ice = int(ice)
light = int(light)

for i in range(n):
    i = input()
    if i=="standard":
        h-=standard
    if i=="fire":
        h-=fire
    if i=="ice":
        h-=ice
    if i=="light":
        h-=light
if h<=0:
    print("dead")
else:
    print(h)
