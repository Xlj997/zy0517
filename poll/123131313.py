
import time

# print(dir(time.clock()))


def qqq(qq):

    def aaa(a):
        time.perf_counter()
        qq(a)
        print(time.perf_counter())
    return aaa


@qqq
def func1(a):
    for i in range(a):
        print(i)


@qqq
def func2(a):
    for i in range(a):
        print(i)



# func1()
# func2(10000)



