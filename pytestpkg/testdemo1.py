# Ensure that PYTEST is installed before using it here. To install, run following command:
# pip3 install pytest

import pytest


@pytest.fixture()
def setUp1():
    print("This setup1 runs before every method")


@pytest.fixture()
def setUp2():
    print("This setup2 runs before every method")


def test_method1(setUp1, setUp2):
    print("This is Method 1 from Test Demo 1 file.")


def test_method2(setUp1, setUp2):
    print("This is Method 2 from Test Demo 1 file.")
