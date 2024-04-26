


def fib(n):
    # base case

    if n == 1 or n == 0:
        return n


    return fib(n-1) + fib(n-2)

print(fib(35))


