#move all zeroes from array to the last retaining all the non zero elements in proper order
nums = [1, 0, 2, 4, 3, 0, 0, 3, 5, 1]
"""
def moveZeroes(nums):
        
        Do not return anything, modify nums in-place instead.
        
        n = len(nums)
        temp = []
        for i in nums:
            if i != 0:
                temp.append(i)
        for i in range(len(temp)):
            nums[i] = temp[i]
        for i in range(len(temp), n):
            nums[i] = 0            
        return nums

"""

#Optimal Solution
def moveZeroes(nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        k = 0
        for i in range(len(nums)):
                if nums[i] != 0:
                        nums[k] = nums[i]
                        k += 1
        
        while k < len(nums):
                nums[k] = 0
                k += 1
        return nums

print(moveZeroes(nums))

