#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Pizza(object):

    @staticmethod
    def mix_ingredients(x, y):
        return x + y

    def cook(self):
        return self.mix_ingredients(self.cheese, self.vegetables)