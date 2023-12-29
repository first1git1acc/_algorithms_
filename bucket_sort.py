def bucket_sort(arr):
    n = len(arr)
    bucket = [list() for _ in range(n)]

    for j in arr:
        index_b = j//10
        bucket[index_b].append(j)

    for i in range(len(arr)):
        bucket[i] = sorted(bucket[i])

    k = 0
    for i in range(len(arr)):
        for j in range(len(bucket[i])):
            arr[k] = bucket[i][j]
            k += 1
    return arr


arr = [int(i) for i in input('Enter array of integer numbers : ').split()]

print('Array before sorting : ',*arr)
print('Array after sorting : ',*bucket_sort(arr))