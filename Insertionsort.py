import timeit

start_time=timeit.default_timer()

def insertionsort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1

        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key

arr=[12,11,13,5,6]
print("Given array is:", arr)
insertionsort(arr)
print("The sorted array is: ", arr)
time1 = timeit.default_timer() - start_time
print("It took", time1, "seconds")
