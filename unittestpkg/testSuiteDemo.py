import unittest

# Import the Classes of Test Cases
from Selenium.unittestpkg.unittest_demo import UnitTestDemo as utd
from Selenium.unittestpkg.unittest_demo_dup import UnitTestDemoDupl as utdd

# Load all test cases/methods from the Classes
utd_tc = unittest.TestLoader().loadTestsFromTestCase(utd)
utdd_tc = unittest.TestLoader().loadTestsFromTestCase(utdd)

# Create the Test Suite
smoke_test = unittest.TestSuite([utd_tc, utdd_tc])

# Associate a Test Runner for executing the Test Suite
unittest.TextTestRunner().run(smoke_test)
