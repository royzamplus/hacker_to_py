#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mock
import os


def fake_os_unlink(path):
    raise IOError("Testing!")

with mock.patch('os.unlink', fake_os_unlink):
    os.unlink('foobar')
