import time

#defining count function
def count(n):
    for i in range(0,n):
        a = n * 10

# code to evaluate run time of function call count(n)
start_time = time.time()
print(start_time)
count(1000000) # timing this function call/executiom
end_time = time.time()
print(end_time)