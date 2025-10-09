'''
Find Numbers with Even Number of Digits [Leetcode Easy]

Example 1:

Input: nums = [12,345,2,6,7896]
Output: 2
Explanation: 
12 contains 2 digits (even number of digits). 
345 contains 3 digits (odd number of digits). 
2 contains 1 digit (odd number of digits). 
6 contains 1 digit (odd number of digits). 
7896 contains 4 digits (even number of digits). 
Therefore only 12 and 7896 contain an even number of digits.
 

'''
nums = [12, 2, 222, 34, 1234, 22, 234]
def lol(nums):
    ans = 0
    for i in nums:
        count = 0
        while i > 0:
            i //= 10
            count += 1
        if count % 2 == 0:
            ans += 1
    return ans
        
print(lol(nums))