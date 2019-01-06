################################################################################
#
# Map, reduce, filter, and functools
#
################################################################################

import functools
import operator
import time
from collections import namedtuple

# the operator module provides a methods for each of the standard intrinsic operators

# so instead of writing something like this for factorial


def fact(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res


print(fact(5))

# or even like this with functools.reduce and a lambda


def fact_lambda(n):
    return functools.reduce(lambda x, y: x * y, range(1, n+1))

# you can write factorial the following way


def fact_op(n):
    return functools.reduce(operator.mul, range(1, n+1))


print(fact_op(5))


# performance wise they are roughly the same

trials = 100000
fact_st = time.time()
fact(trials)
fact_et = time.time()

fact_lambda_st = time.time()
fact_lambda(trials)
fact_lambda_et = time.time()

fact_op_st = time.time()
fact_op(trials)
fact_op_et = time.time()

print(f"factorial execution time: {fact_et - fact_st}")
print(f"factorial (functools/lambda version) execution time: {fact_lambda_et - fact_lambda_st}")
print(f"factorial(functools/operator.mul version) execution time: {fact_op_et - fact_op_st}")

# additionally operator provides some nice conveniences for accessing member is tuples and objects

# if you want to use higher-order functions on tuples (based on a particular tuple value)
# you can use itemgetter, which internally creates a function object to access that particular
# value in each tuple

people = [
    ("John", "Doe", 35),
    ("Jane", "Doe", 29),
    ("David", "Robinson", 53),
    ("Jeff", "Coolidge", 42)
]

# sort people by age

sorted(people, key=operator.itemgetter(2))

# sort people by last name

sorted(people, key=operator.itemgetter(1))

# to access attribute members from objects and class instances we can use attrgetter

Person = namedtuple('Person', 'fname lname age')

people = [
    Person("John", "Doe", 35),
    Person("Jane", "Doe", 29),
    Person("David", "Robinson", 53),
    Person("Jeff", "Coolidge", 42)
]

# sort people by age

sorted(people, key=operator.attrgetter('age'))

# sort people by last name

sorted(people, key=operator.attrgetter('lname'))

# simple of example of using map
# you can use map with a named function


def double(a):
    return 2*a


alist = range(11)
doubles = map(double, alist) # returns an iterable object

class C: pass

obj = C()

print(set(dir(doubles)) - set(dir(obj)))
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

