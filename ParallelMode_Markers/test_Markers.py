# 8 test cases are there to run a specific test use "@pytest.mark.(Name)"

# "py.test -m case"  = @py.test -m is for marker and name of marker

# py.test -m case

import pytest


def test_Case1():
    assert True


def test_Case2():
    assert True


@pytest.mark.case
def test_Case3():
    assert True


def test_Case4():
    assert True


@pytest.mark.case
def test_Case5():
    assert True


def test_Case6():
    assert True


def test_Case7():
    assert True


@pytest.mark.case
def test_Case8():
    assert False
