def insertion_sort(arr,n):
    if n <= 1:
        return arr
    
    for i in range(1,n):
        main = arr[i]
        j = i-1
        print('main = ',main,' j = ',j)
        while j>=0 and main < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
            print('in while',arr)
        arr[j+1] = main
        print('not in while :',arr)

    #return arr

arr = [int(i) for i in input('Enter array of integer numbers : ').split()]

print('Array before sorting : ',*arr)
#print('Array after sorting : ',*insertion_sort(arr,len(arr)))
insertion_sort(arr,len(arr))