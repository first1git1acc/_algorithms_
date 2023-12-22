def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]

    return arr

arr = [int(i) for i in input('Enter array of integer numbers : ').split()]

print('Array before sorting : ',*arr)
print('Array after sorting : ',*bubble_sort(arr))