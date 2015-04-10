#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mock
import requests
import testscenarios


class WhereIsPythonError(Exception):
    pass


def is_python_still_a_programming_language():
    r = requests.get("http://python.org")
    if r.status_code == 200:
        return 'Python is a programming language' in r.content
    raise WhereIsPythonError("Something bad happened")


def get_fake_get(status_code, content):
    m = mock.Mock()
    m.status_code = status_code
    m.content = content
    def fake_get(url):
        return m
    return fake_get


class TestPythonErrorCode(testscenarios.TestWithScenarios):
    scenarios = [
        ('Not found', dict(status=404)),
        ('Client error', dict(status=400)),
        ('Server error', dict(status=500)),
    ]

    def test_python_status_code_handling(self):
        # python -m unittest -v test_scenarios
        with mock.patch('requests.get', get_fake_get(
                                        self.status, 'Python is a programming language for sure')):
            self.assertRaises(WhereIsPythonError, is_python_still_a_programming_language)