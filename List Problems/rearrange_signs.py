"""
Problem: Rearrange Elements by Sign

You are given a 0-indexed integer array `nums` of even length `n`.

The array consists of an equal number of positive and negative integers.

Your task is to rearrange the elements of `nums` such that:

1. Every consecutive pair of integers has opposite signs.
2. For all integers with the same sign, their relative order in `nums` should remain the same as in the original array.

Return the array formed after rearranging the elements.

Example 1:
Input: nums = [3,1,-2,-5,2,-4]
Output: [3,-2,1,-5,2,-4]
Explanation: The positive integers in order are [3,1,2].
The negative integers in order are [-2,-5,-4].
The output alternates between positive and negative integers.

Example 2:
Input: nums = [-1,1]
Output: [1,-1]

Constraints:
- `n == nums.length`
- `2 <= n <= 2 * 10^5`
- `n` is even
- `nums` consists of equal number of positive and negative integers
- Each integer in nums is non-zero

Note:
- Maintain the relative order of positives and negatives.
- Alternate the signs starting with a positive number.
"""

nums = [5, 2, -3, -2, 6, 7, -9, 4, -7, -8]
def rearrange(nums):
    pos = []
    neg = []
    result = []
    for i in range(len(nums)):
        if nums[i] > 0:
            pos.append(nums[i])
        if nums[i] < 0:
            neg.append(nums[i])
    
    l=0
    r=0
    while l < len(pos) and r < len(neg):
        result.append(pos[l])
        result.append(neg[r])
        l += 1
        r += 1
    
    while l < len(pos):
        result.append(pos[l])
        l += 1

    while r < len(neg):
        result.append(neg[r])
        r += 1

    return result

def rearrangeopt(nums):
        pos = 0
        neg = 1
        res = [0]*len(nums) #Hashing
        for num in nums:
            if num > 0:
                res[pos] = num
                pos += 2
            else:
                res[neg] = num
                neg += 2
        return res


[5, 2, -3, -2, 6, 7, -9, 4, -7, -8]

print(rearrangeopt(nums))