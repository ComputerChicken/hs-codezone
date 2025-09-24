nums = [int(i) for i in input().split(",")]
nums.remove(max(nums))
print(max(nums))