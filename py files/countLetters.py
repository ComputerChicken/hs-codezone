alphabet = "qwertyuiopasdfghjklzxcvbnm"
letters = {}
for i in input().lower():
    try:
        if(i in alphabet):
            letters[i] += 1
    except KeyError:
        letters[i] = 1

print(letters)