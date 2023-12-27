def my_version_counting_sort(arr):
    n = len(arr)
    count = [0] * (max(arr)+1)
    output = []

    for i in range(n):
        count[arr[i]] += 1

    if count[0] != 0:
        for_extend = [0] * count[0]
        output.extend(for_extend)

    for i in range(1,max(arr)+1):
        if count[i] != 0:
            for_extend = [i] * count[i]
            output.extend(for_extend)

    return output

def counting_sort(arr):
    n = len(arr)
    count = [0] * (max(arr) + 1)
    output = [0] * n

    for i in range(n):
        count[arr[i]] += 1

    for i in range(1,max(arr)+1):
        count[i] += count[i-1]

    for i in reversed(arr):
        output[count[i]-1] = i
        count[i] -= 1
    
    return output
            
    

arr = [int(i) for i in input('Enter array of integer numbers : ').split()]

print('Array before sorting : ',*arr)
print('Array after sorting mv: ',*my_version_counting_sort(arr))
print('Array after sorting : ',*counting_sort(arr))