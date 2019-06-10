import pytest


@pytest.mark.run(order=1)
def test_method1(sessionSetUp, moduleSetUp, setup):
    print("This is method 1")


@pytest.mark.run(order=4)
def test_method2(sessionSetUp, moduleSetUp, setup):
    print("This is method 2")


@pytest.mark.run(order=2)
def test_method3(sessionSetUp, moduleSetUp, setup):
    print("This is method 3")


@pytest.mark.run(order=5)
def test_method4(sessionSetUp, moduleSetUp, setup):
    print("This is method 4")


@pytest.mark.run(order=3)
def test_method5(sessionSetUp, moduleSetUp, setup):
    print("This is method 5")