################################################################################
#
# Iterators and iterables overview
#
################################################################################

# The iterator protocol in Python allows one to be able to write Objects that can
# are lazy evaluated and can perform as if they were proper lazy data structures
# such as those in Haskell. For this to work one must implement these Objects a particular
# way.

# For example, in Haskell, streams are infinite sequences that can be indexed into as well
# iterated through.
#
# Below is an example that will illustrate the equivalent haskell code in Python:
#
# x = [1..]
# y = take 10 x

# the collections module provides many built-in objects and classes
import itertools
from collections import Sequence

class IntStream(Sequence):
    def __init__(self, init_value, stepsize):
        self.it = itertools.count(init_value, stepsize)
        self._cache = []
    def __getitem__(self, index):
        while len(self._cache) <= index:
            self._cache.append(next(self.it))
        return self._cache[index]
    def __len__(self):
        return len(self._cache)

# example of usage
ints = IntStream(0, 1)
first_ten = [x for _, x in zip(range(10), ints)]

print(first_ten)
# We can generalized the above code to the following Sequence subclass
# (code from "Functional Programming in Python" by David Mertz)
class ExpandingSequence(Sequence):
    def __init__(self, it):
        self.it = it
        self._cache = []
    def __getitem__(self, index):
        while len(self._cache) <= index:
            self._cache.append(next(self.it))
        return self._cache[index]
    def __len__(self):
        return len(self._cache)

################################################################################
#
# Essence of Iterator pattern
#
################################################################################

# The best way of creating iterator to create a Generator function
def to100():
    for x in range(100):
        yield x

#
# the above code will create a generator object that implements the iterator protocol
# (that is implements __iter__ or __next__ or both)
#

implementsIteration = '__iter__' in dir(to100())
print(implementsIteration)

################################################################################
#
# itertools overview
#
# itertools is a nice module that contains a bunch of very powerful functions
# for performing very sophisticated operations on iterators without paying the
# the computational overhead cost until it is absolutely necessary.
#
################################################################################

# other functions available in itertools

# example of infinite integer stream with count
astream = itertools.count(0, 1)

# because Python doesn't have a take function, we can mimic by using a combination
# of zip (which creates tuples between two sequences) and a finite range, and ignore
# the first argument from the pair return value of the zip collection we are looping through.
alist = [x for _, x in zip(range(10), astream)]

# Another way of grabbing a sample of the stream using takewhile and a lambda
blist = itertools.takewhile(lambda x: x < 10, astream)
clist = itertools.takewhile(lambda x: x < 10, astream)

# in all cases, there is a little gotcha with the above code. 
print(alist == blist) # what do you think the result would be here

#
