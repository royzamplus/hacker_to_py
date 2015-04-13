#!/usr/bin/env python
# -*- coding: utf-8 -*-

stringlist = ["I think", "I'm good"]

# map usage
map(lambda x: x + "bzz!", stringlist)

list(map(lambda x: x + "bzz!", stringlist))
# >>["I thinkbzz!", "I'm goodbzz!"]

# equivalent of map using list comprehension
(x + "bzz!" for x in stringlist)
[x + "bzz!" for x in stringlist]

# filter usage
filter(lambda x: x.startswith("I "), stringlist)

list(filter(lambda x: x.startswith("I "), stringlist))
# >>["I think"]

# equivalent of map using list comprehension
(x for x in stringlist if x.startswith("I "))
[x for x in stringlist if x.startswith("I ")]

mylist = [0, 1, 3, -1]

# enumerate usage
for i, item in enumerate(mylist):
    print "Item %d: %s" % (i, item)

# all usage
if all(map(lambda x: x > 0, mylist)):
    print "All items are greater than 0"

# any usage
if any(map(lambda x: x > 0, mylist)):
    print "At least one item is greater than 0"

keys = ["foobar", "barzz", "ba!"]

# zip usage
map(len, keys)
zip(keys, map(len, keys))
list(zip(keys, map(len, keys)))
# >>[('foobar', 6), ('barzz', 5), ('ba!', 3)]
dict(zip(keys, map(len, keys)))
# >>{'foobar': 6, 'barzz': 5, 'ba!': 3}


def first(predicate, items):
    for item in items:
        if predicate(item):
            return item

first(lambda x: x > 0, [-1, 0, 1, 2])

# using first
from first import first

first([-1, 0, 1, 2], key=lambda x: x > 0)