#Merge two sorted lists, without duplicate elements
nums1 = []
nums2 = [2, 2, 2,]
def merge(nums1, nums2):
    res = []
    i = 0
    j = 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            if nums1[i] not in res:
                res.append(nums1[i])
            i += 1
        elif nums1[i] == nums2[j]:
            if nums1[i] not in res:
                res.append(nums1[i])
            i+=1
            j+=1
        elif nums1[i] > nums2[j]:
            if nums2[j] not in res:
                res.append(nums2[j])
            j+=1

    while i < len(nums1):
        if nums1[i] not in res:
            res.append(nums1[i])
        i+=1

    while j < len(nums2):
        if nums2[j] not in res:
            res.append(nums2[j])
        j+=1
    
    return res

print(merge(nums1, nums2))