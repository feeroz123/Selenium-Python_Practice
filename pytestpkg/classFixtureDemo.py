# Ensure that PYTEST is installed before using it here. To install, run following command:
# pip3 install pytest

import pytest


@pytest.mark.usefixtures("sessionSetUp", "moduleSetUp", "classSetUp", "setup")  # Not necessary to use all fixtures from conftest
class Test_ClassFixture():

    # Creating a fixture inside the class and making it auto-use for all test methods.
    @pytest.fixture(autouse=True)
    def class_fixture_auto(self):
        self.a = 10
        self.b = 5
        print("This is a class fixture set for auto use in all methods")

    def test_method1(self):
        c = self.a + self.b
        assert c == 15
        print("This is Method 1 : ", c)

    def test_method2(self):
        c = self.a - self.b
        assert c == 5
        print("This is Method 1 : ", c)
