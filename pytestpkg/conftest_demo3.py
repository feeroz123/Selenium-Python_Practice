"""
The methods defined below make use of the Yield Fixtures defined in "conftest.py" file
"""

def test_method1(moduleSetUp, setup):
    print("This is Method 1")


def test_method2(moduleSetUp, setup):
    print("This is Method 2")
