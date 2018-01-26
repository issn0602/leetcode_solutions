"""
Given a sorted array, remove the duplicates in-place such that each element
appear only once and return the new length.
Do not allocate extra space for another array, you must do this by modifying
the input array in-place with O(1) extra memory.

"""

def removeDuplicates(nums):
    if not nums:
        return 0
    i, j = 0, 1
    while j < len(nums):
        if nums[i] != nums[j]:
            i+=1
            nums[i] = nums[j]
        j+=1
    print(nums)
    return i+1