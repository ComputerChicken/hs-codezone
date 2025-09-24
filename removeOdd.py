string = input()
lowerString = string.lower()
newString = ""
outString = string.split()
for char in lowerString:
    if char.isalpha() or char == " ":
        newString += char
count = 0
for word in newString.split():
    if(len(word) % 2 == 1):
        toRemove = newString.split().index(word) - count
        outString.pop(toRemove)
        count += 1

print(" ".join(outString))