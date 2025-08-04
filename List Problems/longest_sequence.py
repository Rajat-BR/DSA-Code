'''
Problem: Longest Consecutive Sequence

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example:
Input: nums = [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore, its length is 4.
'''

nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
arr = [100, 4, 200, 1, 2, 3]

def longest(nums):
    lol = set(nums)
    current = 0
    longest = 0 
    for n in lol:
        if n - 1 not in lol:
            current = n
            length = 1
            while current + 1 in lol:
                current += 1
                length += 1
            longest = max(longest, length)
            
    return longest



print(longest(nums))

#Can i build streak only if there's no smaller number before this ?