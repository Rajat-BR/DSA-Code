#Find the missing number in an array
# given array with n distinct elements. find the missing number between the range of [0, n]
nums = [0, 1, 3, 4, 5, 6, 7, 8, 9]
def miss(nums): #Brute Force (This is correct but slow af)
    n = len(nums)
    for i in range(0, len(nums)+1):
        if i not in nums:
            return i
        
def miss2(nums): # Optimal Solution 
    n = len(nums)
    expected_sum = n*(n+1) // 2
    return expected_sum - sum(nums)

#The toal sum of first n whole numbers - total sum with missing number gives thw missing number as answer
        

print(miss2(nums))
print(miss(nums))