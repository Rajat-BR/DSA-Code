'''
Squares of a Sorted Array [LeetCode Easy]

Solution
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11] res = [,9,49,121]
Output: [4,9,9,49,121]
 
'''
'''

result = []
def lol(nums):
    for num in nums:                This is a bad Code
        result.append(num**2)
    return sorted(result)

print(lol(nums))

'''
nums = [-4, -1, 0, 3, 10]
def lol(nums):
    n = len(nums)
    result = [0]*n
    i = 0
    j = n - 1
    pos = n - 1
    while i <= j:
        isq = abs(nums[i])**2
        jsq = abs(nums[j])**2
        if isq < jsq:
            result[pos] = jsq
            j -= 1
            pos -= 1
        else:
            result[pos] = isq
            i += 1 
            pos -= 1   
    return result

print(lol(nums))