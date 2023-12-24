def selection_sort(arr,n):
    for i in range(n):
        for j in range(i+1,n):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

arr = [int(i) for i in input('Enter array of integer numbers : ').split()]

print('Array before sorting : ',*arr)
print('Array after sorting : ',*selection_sort(arr,len(arr)))