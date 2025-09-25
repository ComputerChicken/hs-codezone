nums = [int(i) for i in list(input())]
while len(str(sum(nums))) != 1:
    nums = [int(i) for i in str(sum(nums))]
print(str(sum(nums)))