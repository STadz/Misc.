import timeit

def speed_test_while():
    i = 0
    s = 0
    while i < 1_000_000:
        s += i
        i += 1
    return s


def speed_test_for():
    s = 0
    for i in range(1_000_000):
        s += i
    return s


def speed_test_builtin():
    return sum(range(1_000_000))



print("while loop speed: ", timeit.timeit(speed_test_while, number=1))
print("for loop speed: ", timeit.timeit(speed_test_for, number=1))
print("builtin sum speed: ", timeit.timeit(speed_test_builtin, number=1))