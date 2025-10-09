#Difficulty : Easy
#Find the largest element in an Array
arr = [12, 45, 32, 69, 99,66, -9]
def large(arr):
    largest = arr[0]
    for i in range(0, len(arr)):
        largest = max(largest, arr[i])
    return largest

print(large(arr))

#Find the second largest element in an array without sorting
def sec(arr):
    largest = float("-inf")
    second = float("-inf")
    for i in range(0, len(arr)): #iterate only one time
        if arr[i] > largest:
            second = largest
            largest = arr[i]
        elif arr[i] > second:
            second = arr[i]
            
    return second

print(sec(arr)) 
