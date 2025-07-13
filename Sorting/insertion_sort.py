#we can sort the elements by inserting the smaller element to its correct possition
#by shifiting all the sorted elements and inserting the unsorted element
arr = [3,4,2,1,6,5,8,0,9,7]
def insertion_sort(arr):
    n = len(arr)
    for i in range(1,n):
        key = arr[i]
        j = i-1
        while j >=0 and arr[j]>key:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key
    return arr

print(insertion_sort(arr))