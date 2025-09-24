alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
phrase = input()
shift = int(input())
total = ""
for i in phrase:
    if(i in alphabet):
        curIndex = alphabet.index(i)
        newIndex = 0
        if(26 > curIndex >= 26 - shift):
            newIndex = curIndex - 26 + shift
        elif(curIndex >= 52 - shift):
            newIndex = curIndex - 26 + shift
            print(newIndex)
        else:
            newIndex = curIndex + shift
        total += alphabet[newIndex]
    else:
        total += i
print(total)
