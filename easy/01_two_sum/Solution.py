class Solution:
    def twoSum(self, nums, target):
        n = len(nums)
        for i in range(n-1):
            temp = target - nums[i]
        if temp in nums[i+1:]:
            return [ i, nums[i+1:].index(temp)+i+1 ]