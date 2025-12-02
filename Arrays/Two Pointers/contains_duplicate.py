nums = [1, 3, 4, 2, 5, 7, 6, 8, 9]

duplicate = {}
n = len(nums)
def contains_duplicate(nums):
    for i in nums:
        duplicate[i] = duplicate.get(i, 0) + 1
        if duplicate[i] > 1:
            return True
    return False
print(contains_duplicate(nums))
