nums = [int(i) for i in input().split(",")]
odds = 0
evens = 0
for i in nums:
    if(i % 2 == 0):
        evens += 1
    else:
        odds += 1

if(odds > evens):
    for i in nums:
        if(i % 2 == 0):
            print(i)
            break
else:
    for i in nums:
        if(i % 2 == 1):
            print(i)