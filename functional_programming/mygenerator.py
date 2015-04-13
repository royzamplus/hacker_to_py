#!/usr/bin/env python
# -*- coding: utf-8 -*-

import inspect


def mygenerator():
    yield 1
    yield 2
    yield 'a'


g = mygenerator()
print next(g)
print next(g)
print next(g)

# StopIteration
# print next(g)

print inspect.isgeneratorfunction(mygenerator)

print inspect.isgeneratorfunction(sum)