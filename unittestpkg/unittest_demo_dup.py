import unittest

class UnitTestDemoDupl(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("Runs Once before the Class")


    def setUp(self):
        print("Runs before every test case")

    def test_tc1(self):
        print("This is Test case 1")

    def test_tc2(self):
        print("This is Test case 2")

    def test_tc3(self):
        print("This is Test case 3")


    def tearDown(self):
        print("Runs after every test case")

    @classmethod
    def tearDownClass(cls):
        print("Runs Once after the Class")


# To run this class directly as the Main method
if __name__ == "__main__":
    unittest.main(verbosity=2)