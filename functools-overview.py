################################################################################
#
# Map, reduce, filter, and functools
#
################################################################################

import functools

dir(functools)

# simple of example of using map
# you can use map with a named function
def double(a):
    return 2*a


alist = range(0,11)
doubles = map(double, alist)

print(doubles)

# or you can simply use a lambda
triples = map(lambda x: 3*x, alist)

print(triples)

# functools.reduce in Python3 (backported in Python2) has reduce as well
another_sum = functools.reduce(lambda a,x: a+x, alist)
print(another_sum)

# example of using filter
evens = filter(lambda x: x%2 == 0, alist)
print(evens)

# example of partial application with another adder example


def multiply(a,b):
    return a * b


double = functools.partial(multiply, 2)
print(double(2))

