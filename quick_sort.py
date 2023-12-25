def swap(arr,start,end):
    main = arr[end]
    i = start - 1
    for j in range(start,end):
        if arr[j]<=main:
            i += 1
            arr[i],arr[j] = arr[j],arr[i]

    arr[i+1],arr[end] = arr[end],arr[i+1]

    return i+1

def quick_sort(arr,start,end):
    if end > start:
        p = swap(arr,start,end)
        quick_sort(arr,start,p-1)
        quick_sort(arr,p+1,end)
    return arr

arr = [int(i) for i in input('Enter array of integer numbers : ').split()]

print('Array before sorting : ',*arr)
print('Array after sorting : ',*quick_sort(arr,0,len(arr)-1))