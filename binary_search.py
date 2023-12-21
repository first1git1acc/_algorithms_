import time

start = time.time()
 
def binary_search(array, search, begin, end, step):

    middle = (begin + end)//2
    print(f'begin : {begin} , end : {end} , step {step}')
    if begin>end:
        return f'number {search} not in array'

    if array[middle] == search:
        return f'number {search} in array with index : {middle}'
    elif array[middle]>search:
        return binary_search(array, search, begin, middle - 1, step + 1)
    elif array[middle]<search:
        return binary_search(array, search, middle + 1, end, step + 1)
    
array = [float(i) for i in input('Enter array  integer or real numbers : ').split()]
search = float(input('Enter number which you want search in array :'))

print(binary_search(sorted(array),search,0,len(array)-1,0))

end = time.time()

print(f'algorithm time = {end-start}ms')