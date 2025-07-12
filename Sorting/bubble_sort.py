#Bubble sort bubbles out the largest element towards right in every pass
arr = [1,9,8,4,5,6,3,2,0,7]
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False #resets every pass
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped: #early exit
            break
    return arr

print(bubble_sort(arr))