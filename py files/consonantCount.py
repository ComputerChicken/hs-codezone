inp = input().split()
counter = 0
for word in inp:
    if word[0].lower() not in "aeiou":
        counter += 1
print(counter)