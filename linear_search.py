#Linear Search, return the index of the elements to be searched
nums = [1, 4, 13, 43, 5, 87, 69, 45, 43, 23, 12]

def linearsearch(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1

print(linearsearch(nums, 43))