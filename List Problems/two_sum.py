#hint if is[i] = x then seaarch for element that is target - x
def twoSum(nums, target): #TC is O(N2)
    
    for i in range(len(nums)):
        
        compliment = target - nums[i]
        if nums[i+1] == nums[i] and nums[i] + nums[i+1] == target:
            return [i+1, i+2]
        if compliment in nums and i != nums[i]:
            return [i+1, nums.index(compliment)+1]
        

    
    

nums = [1,2,3,4,4,9,56,90]


print(twoSum(nums, 8))


