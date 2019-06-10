# Ensure that PYTEST is installed before using it here. To install, run following command:
# pip3 install pytest

import pytest


@pytest.yield_fixture()
def setup():
    print("This step runs before each method")
    yield
    print("This step after 'yield' keyword runs after each method")


def test_method1(setup):
    print("This is Method 1 from Test Demo 2 file.")


def test_method2(setup):
    print("This is Method 2 from Test Demo 2 file.")