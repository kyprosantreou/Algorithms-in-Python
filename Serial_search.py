import timeit

start_time=timeit.default_timer()

def serial_search(A,item):
    for x in A:
        if x==item:
            return "Found"
        if x>item:
            return "Not found"
    return "Not found"

List=[u for u in range(1,101)]

P=serial_search
print(P)

time1=timeit.default_timer()-start_time

print("It took",time1,"seconds")