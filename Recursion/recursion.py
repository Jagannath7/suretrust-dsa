

def factorial(n):

    # Base Case
    if n < 2:
        return 1

    return n * factorial(n-1)


def nToOne(n):

    if n < 1:
        return

    print(n)
    nToOne(n-1)


def oneToN(n):

    if n<1:
        return

    oneToN(n-1)
    print(n)


def decInc(n):

    if n<1:
        return

    print(n)
    incDec(n-1)
    print(n)


def incDec(n, current = 1):

    # base case
    if current > n:
        return

    print(current)
    incDec(n, current+1)
    print(current)


# incDec(5)


