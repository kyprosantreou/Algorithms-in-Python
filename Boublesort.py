import timeit

start_time=timeit.default_timer()

def bubblesort(nlist):
    N=len(nlist)
    for i in range(N-1):
        for j in range(N-i-1):
            if nlist[j]>nlist[j+1]:
                temp=nlist[j]
                nlist[j]=nlist[j+1]
                nlist[j+1]=temp

nlist=[14,46,43,27,57,41,45,21,70]
bubblesort(nlist)
print(nlist)
time1=timeit.default_timer()-start_time
print("It took",time1,"secconds")

