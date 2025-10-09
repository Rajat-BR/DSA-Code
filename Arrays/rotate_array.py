#Rotate array by 1 time
nums = [1, 2, 3, 4, 5, 6, 7]

#Rotated array should be [7, 1, 2, 3, 4, 5 ,6]
#1. Rotate using Slicing
n = len(nums)
nums = nums[-1:] + nums[:n-2] # this creates a new variable for nums

#in order to rotate it in-Place then use
nums[:] = nums[-1:] + nums[:n-2] 

#2. Rotate using for loop
temp = nums[len(nums)-1]
for i in range(len(nums)-2,-1, -1):
    nums[i+1] = nums [i]
nums[0] = temp
print(nums)