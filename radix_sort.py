
def radix_sort(arr):
    n = len(arr)
    maxLength = False
    tmp , placement = 0, 1

    while not maxLength:
        maxLength = True
        output = [list() for _ in range(n)]

        for  i in arr:
            tmp = i // placement
            output[tmp % n].append(i)
            if maxLength and tmp > 0:
                maxLength = False
        print('This output list :',*output)

        a = 0
        for b in range(n):
            buck = output[b]
            for i in buck:
                arr[a] = i
                a += 1

        placement *= n
    return arr

arr = [int(i) for i in input('Enter array of integer numbers : ').split()]

print('Array before sorting : ',*arr)
print('Array after sorting : ',*radix_sort(arr))