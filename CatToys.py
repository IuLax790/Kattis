import math
nums = input().split()
nums[0] = int(nums[0]) ; nums[1] = int(nums[1])

if nums[0]>nums[1]:
    print(math.ceil(nums[0]/nums[1]))
else:
    print(math.ceil(nums[0]/nums[1]))
