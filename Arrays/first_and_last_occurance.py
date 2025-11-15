"""              ------------LEETCODE 34------------

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]


"""
nums = []
def searchRange( nums, target):
    def lower_bound():
        l, r = 0, len(nums) - 1
        ans = -1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] >= target:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans
    
    def upper_bound():
        l, r = 0, len(nums) - 1
        ans = -1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > target:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans
    
    lb = lower_bound()
    if lb == -1 or nums[lb] != target:
        return [-1, -1]
    
    ub = upper_bound()
    
    if ub == -1:
        ub = len(nums)
    
    return [lb, ub - 1]


print(searchRange(nums, 0))