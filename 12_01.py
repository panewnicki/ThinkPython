# simply code, fail if type(args) == list or tuple
def sumall(*args):
	a = tuple(args)
	return sum(a)

# for tuples and lists
# inspriation: https://www.geeksforgeeks.org/python-unpacking-nested-tuples/?ref=rp
from functools import reduce
import numpy

def sumall_universal(*args):
    b = tuple(reduce(numpy.append, args))
    return sum(b)

