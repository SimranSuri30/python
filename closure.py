# for persistant states
def counter():
    # value of message is present here
    count = 0
    def increment():
        nonlocal count 
        count += 1
        print(count)

    return increment

c1 = counter()
c1()
c1()

c2 = counter()

c2()
c1()



