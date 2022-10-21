

def twoSum(nums, target):
    for i1 in range(0, len(nums) - 1):
        for i2 in range(i1 + 1, len(nums)):
            if nums[i1] + nums[i2] == target:
                return [i1, i2];
    return None


nums = [3, 2, 4]
target = 6

result=twoSum(nums, target)

print(result)