import functools
import operator

################################################################################
#
# Recursion overview
#
################################################################################

# factorial example


def factorial(N):
    assert isinstance(N, int) and N >= 1
    return 1 if N <= 1 else N*factorial(N-1)

# clearly this would blow up the recursive stack if we create stack depths > 1000.
# in general this style is discouraged and replaced with a more iterative style


def factorial_iterative(N):
    result = 1
    while N > 1:
        result, N = result*N, N-1
    return result

# in python though, the fastest implementation in fact is a functional style
# factorial that uses reduce (compliments of "Functional Programming in Python" by David Mertz)


def factorial_reduce(N):
    return functools.reduce(operator.mul, range(1, N+1))

# using recursion, one can make an entire program based on a simple recursive expressive.


def identity_print(x):
    print(x)
    return x


afunc = lambda: identity_print(input("FP --- ")) == 'quit' or afunc()
afunc()
