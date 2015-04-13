#!/usr/bin/env python
# -*- coding: utf-8 -*-

import operator
from first import first


def greater_than_zero(number):
    return number > 0


first([-1, 0, 1, 2], key=greater_than_zero)

