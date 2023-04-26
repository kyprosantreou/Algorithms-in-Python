import timeit

start_time=timeit.default_timer()

def quick_sort(A):
    less=[]
    equal=[]
    greater=[]

    if len(A)>1:
        pivot=A[0]
        for x in A:
            if x<pivot:
                less.append(x)
            elif x==pivot:
                equal.append(x)
            else:
                greater.append(x)
            
        return quick_sort(less)+quick_sort(equal)+quick_sort(greater)
    else:
        return A
        
A=[12, 11, 13, 5, 6, 7, 14, 15, 40, 24]
print("Given array is:", A)
A = quick_sort(A)
print("The sorted array is: ", A)
time1 = timeit.default_timer() - start_time
print("It took", time1, "seconds")
