#Leet Code Problem 
#Rotate Array / List by a factor of K times
def rotate(nums, k) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    k = k % n
    nums[:] = nums[-k:] + nums[:-k]
    return nums

print(rotate([1, 2, 3, 4, 5, 6, 7], 3))

    