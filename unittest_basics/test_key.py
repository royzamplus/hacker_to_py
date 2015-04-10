#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest


class TestKey(unittest.TestCase):
    def test_key(self):
        a = ['a', 'b']
        b = ['b']
        self.assertEqual(a, b)