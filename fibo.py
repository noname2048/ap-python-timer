import datetime
import timeit

def check_time(func):

    def wrapper(*args, **kwargs):
        s = datetime.datetime.now()

        ret = func(*args, **kwargs)

        e = datetime.datetime.now() - s
        print(f"{func.__name__}: {(e.microseconds / 1E+6):.6f}")

        return ret

    return wrapper

def for_timeit_test():
    fibo(50)

@check_time
def fibo(n):

    if (1 <= n <= 2):
        return 1

    a = b = 1
    for i in range(n - 2):
        a, b = b, a + b
        
    return b

def memorization(func):
    cache = list((-1, 1, 1))

    def wrapper(n):
        if n < len(cache):
            return cache[n]
        else:
            s = len(cache)
            e = n
        return func(s, e, cache)

    return wrapper


@memorization
@check_time
def memo_fibo(s: int, e: int, cache):
    a = cache[s - 2]
    b = cache[s - 1]

    for i in range(s, e + 1):
        a, b = b, a + b
        cache.append(b)
    
    return b

if __name__ == "__main__":
    print(fibo(49))
    print(memo_fibo(49))
    print(memo_fibo(50))

    print(timeit.timeit(for_timeit_test, number=100))
