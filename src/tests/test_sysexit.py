'''
Created on 6 ago. 2020

@author: msanavarro
'''
import pytest


def f():
    raise SystemExit(1)


def test_mytest():
    with pytest.raises(SystemExit):
        f()