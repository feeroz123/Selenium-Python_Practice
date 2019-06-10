import unittest

class AssertDemo(unittest.TestCase):

    def test_assertEqual(self):
        a = 'Test'
        b = 'test'
        c = 'Test'
        self.assertEqual(a, c, "Failed. A is not equal to C")
        self.assertNotEqual(a, b, "Failed. A is equal to B")

    def test_assertTrueFalse(self):
        a = True
        b = False
        self.assertTrue(a, "Failed. A is False.")
        self.assertFalse(b, "Failed. B is True.")
        # self.assertTrue(b, "Failed. B is actually False.")
        # self.assertFalse(a, "Failed. A is actually True.")


if __name__ == '__main__':
    unittest.main(verbosity=2)