#!/usr/bin/env python
# -*- coding: utf-8 -*-

import abc


class BasePizza(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_radius(self):
        """Method that should do something."""


class Galzone(BasePizza):
    def get_ingredients(self, with_egg=False):
        egg = Egg() if with_egg else None
        return self.ingredients + [egg]


class DietPizza(BasePizza):
    @staticmethod
    def get_ingredients():
        return None