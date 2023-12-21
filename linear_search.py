import time

start = time.time()

def linear_search(arr,search):
    for i in range(len(arr)):
        if arr[i] == search:
            return f'number {search} in array with index : {i}'
    return f'number {search} is not in array'

arr = [float(i) for i in input('Enter array  integer or real numbers : ').split()]
search = float(input('Enter number which you want search in array :'))

print(linear_search(arr,search))

end = time.time()
print(f'algorithm time = {end-start}ms')