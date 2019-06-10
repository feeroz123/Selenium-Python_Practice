import pytest


@pytest.yield_fixture()
def setup():
    print("This runs before each method")
    yield
    print("This runs after each method")


@pytest.yield_fixture(scope="module")
def moduleSetUp():
    print("This runs before each module")
    yield
    print("This runs after each module")


@pytest.yield_fixture(scope="session")
def sessionSetUp():
    print("This runs once before each session")
    yield
    print("This runs once after each session")


@pytest.yield_fixture(scope="class")
def classSetUp():
    print("This runs once before each Class")
    yield
    print("This runs once after each Class")