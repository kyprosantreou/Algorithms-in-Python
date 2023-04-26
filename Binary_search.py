import timeit

start_time=timeit.default_timer()

def binary_search(A,item):
    first=0
    last=len(A)-1
    found=False

    while first<=last and not found:
        mid=(first+last)//2
        if A[mid]==item:
            return mid
        else:
            if item<A[mid]:
                last=mid-1
            else:
                first=mid+1
    return mid

List=[u for u in range(1,101)]
b=binary_search(List,108)

print(b)

time1=timeit.default_timer()-start_time
print("It took",time1,"seconds")