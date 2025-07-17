#Quick sort, Pick a pivet (any number) and place it in it's corect position
arr = [4, 1, 7, 6, 3, 2, 8]

def partition(arr, low, high):
    pivot = arr[low]
    i = low
    j = high
    while i < j:
        while arr[i] <= pivot and i <= high - 1:
            i += 1
        while arr[j] >= pivot and j >= low + 1:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[low], arr[j] = arr[j], arr[low]
    return j #Sorted successfully

def quick_sort(arr, low, high):
    if low < high:
        p_index = partition(arr, low, high)
        quick_sort(arr, low, p_index-1)
        quick_sort(arr, p_index+1, high)

n = len(arr)
quick_sort(arr, 0, n - 1)
print(arr)

