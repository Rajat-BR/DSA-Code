nums = [2,3,4,5,6,7,8,9,10]
#Iterative Solution
def binaryiterative(nums, target):
    n = len(nums)
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

print(binaryiterative(nums, 8))   #Example

#Recursive Solution
def binaryrecursive(nums, low, high, target):
    if low > high:
        return -1
    mid = (low + high) // 2
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        return binaryrecursive(nums, mid + 1, high, target)
    else:
        return binaryrecursive(nums, low, mid - 1, target)
    
print(binaryrecursive(nums, 0, 8, 10)) #Example


# Time Complexity is O(log2(N)) where N is the number of elements in the list

# for example, lets take there are 32 elements in the list, then this program's loop 
# will run log2(32) = 5 times, if there were 64 elements then the program's loop
# will run log2(64) = 6 times. Therefore the TC -> O(log2(N))

# Space Complexity is O(1) for iterative solution and O(log2(N)) for recursive solution

# Iterative solution is recommended 99% of the times

