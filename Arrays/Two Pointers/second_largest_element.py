# Given an array, find the second largest element in the array, 
# if it dosent exist , return -1
#largest = 100
#sec-largest = 169
nums = [1, 1, 1, 1, 1, 1, 1]
def second_largest(nums):
    largest = -float("inf")
    sec_largest = -float("inf")
    for num in nums:
        if num > largest:
            sec_largest = largest
            largest = num
        elif num < largest and num > sec_largest:
            sec_largest = num
    if sec_largest == -float("inf"):
        return -1
    return sec_largest




print(second_largest(nums))