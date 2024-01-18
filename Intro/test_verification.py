import pytest


def test_m1():
    a = 3
    b = 5
    assert a + b == 6, "Test Failed a+b = b"
    assert a == b, "Failed a == b"


def test_m2():
    name = "shore"
    assert name.upper() == "SHORE"


def test_m3():
    assert 100 == 100
