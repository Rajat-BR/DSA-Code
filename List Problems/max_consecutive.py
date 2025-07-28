#Given a binary array, find the max consecutive 1s in the array
nums = [1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0]
def maxx(nums): # TC is O(N) SC is also O(1) this is optimal
    count = 0
    max_count = 0 
    for i in nums:
        if i == 1:
            count +=1
            if count > max_count:
                max_count = count
        elif i == 0:
            count = 0

    return (max_count)

print(maxx(nums))