# Given an array of integers, return indices of the two numbers such that they 
#add up to a specific target.
# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.

def twoSum(nums, target):
        n = len(nums)
        for i in range(n-1):
            temp = target - nums[i]
            if temp in nums[i+1:]:
                return [ i, nums[i+1:].index(temp)+i+1 ]

nums = [3,2,3]
target = 6

print(twoSum(nums,target))