import pytest


def f(x):
    return x+1


def test_case01():
    assert f(1) == 2
