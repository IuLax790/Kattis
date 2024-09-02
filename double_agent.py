str = input().strip()
smiley = ':)'
frowny = ':('
str = str.replace("  "," ")
print(str)

print("double agent" if smiley in str and frowny in str else "alive" if smiley in str else "undead" if frowny in str else "machine")
