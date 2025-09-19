vowels = "aeiou"
total = ""
for i in input():
    try:
        index = vowels.index(i)
        if(index != 4):
            total += vowels[index+1]
        else:
            total += vowels[0]
    except:
        total += i
        continue
print(total)