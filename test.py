"""test for main.py"""

import os
from main import addition
from main import multiplication
#only import import library
#if you want to import all library from main.py can use * instead
# from main import * or addition, multiplication

def test_file_exists():
    """exists"""
    assert os.path.isfile("./Intro_1.py")


def test_addition_function():
    """"addition"""
    assert addition(3, 5) == 8
    assert addition(2, 3) == 5


def test_multiplication_function():
    """"multiplication"""
    assert multiplication(3, 5) == 15
    assert multiplication(2, 3) == 6

# example command line = pytest -xv test.py