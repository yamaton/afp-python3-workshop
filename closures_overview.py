#!/usr/bin/python -Wall

import functools
import operator

################################################################################
#
# Lambda Expressions, and closures
#
################################################################################


# example of a simple anonymous function in python
add2 = lambda x: x + 2

print(add2(2))

#
# another way of generating functions with a function
# notice this will create a closure and bind the lambda around a which is
# scoped and bound in the outer function before the lambda is constructed.
#
def create_adder(a):
    return lambda b: a + b

add4 = create_adder(4)
add3 = create_adder(3)

print(add4(4))
print(add3(4))

# old way of creating closures without lambdas
def create_adder_old_way(a):
    def adder(b):
        return a + b
    return adder

add5 = create_adder_old_way(5)

print(add5(6))

# example of function that creates functions
def create_greeter():
    """
    Example of creating a function that creates function with
    inner(scoped) function definitions
    """
    def greeter(x):
        print(x)

    return greeter

a = create_greeter()
b = create_greeter()

a('a is called')
b('b is called')

# Gotcha about closures - Python binds variables in closures by "name" not by "value"
# which causes the following code not to behave as intended
adders = []
for x in range(5):
    adders.append(lambda y: x + y)

alist = [adder(10) for adder in adders]
blist = [adder(20) for adder in adders]

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
