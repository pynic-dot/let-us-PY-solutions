def pybasic1():
    a = 2
    b = 4
    print("before swap a is {} and b is {}".format(a, b))
    a, b = b, a
    print("after swap a is {}  and b is {} ".format(a, b))


def pybasic2():
    import math
    x = 30
    print(math.pow(x, 3))
    print(math.sqrt(30))
    print(math.sin(30))
    print(math.sinh(x))


pybasic1()
pybasic2()


def pybasic3():
    import random
    import time      
    random.seed(int(time.time()))
    for x in range(5):
        print(random.randint(10, 50))


pybasic3()
