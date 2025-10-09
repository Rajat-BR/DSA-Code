'''
Duplicate Zeroes [Leetcode]

Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.

 

Example 1:

Input: arr = [1,0,2,3,0,4,5,0]
Output: [1,0,0,2,3,0,0,4]
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
Example 2:

Input: arr = [1,2,3]
Output: [1,2,3]
Explanation: After calling your function, the input array is modified to: [1,2,3]
 
'''
arr = [8,4,5,0,0,0,0,7]

'''
def duplicate(arr):
    n = len(arr)
    i = 0
    while i < n:
        if arr[i] == 0:                     Brute Force 
            j = n - 2                       TC is O(N^2) BAD!!
            while j > i:                    SC is O(1)
                arr[j+1] = arr[j]
                j -= 1
            if i+1 < n:
                arr[i+1] = 0
            i += 2
        else:
            i += 1

    print(arr)

duplicate(arr)
'''

def duplicate(arr):
    zeroes = arr.count(0)
    n = len(arr)
    for i in range(n-1, -1, -1):
        if i + zeroes < n:
            arr[i + zeroes] = arr[i]
        if arr[i] == 0: 
            zeroes -= 1
            if i + zeroes < n:
                arr[i + zeroes] = 0   

    print(arr)

duplicate(arr)


            



