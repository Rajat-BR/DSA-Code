#selection sort 
arr = [1, 5 , 23, 21, 98, 3, 4, 9, 7, 0]
n = len(arr)
def selection_sort(arr):
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i],arr[min_index] = arr[min_index],arr[i]
    return arr

print(selection_sort(arr))