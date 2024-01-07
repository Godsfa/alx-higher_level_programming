import unittest
from max_integer import max_integer

class TestMaxInteger(unittest.TestCase):

    def test_max_integer(self):
        # Test with a list of integers.
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        # Test with a list containing negative and positive integers.
        self.assertEqual(max_integer([-1, -2, 3, 4]), 4)
        # Test with a list of negative integers.
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        # Test with a list containing one integer.
        self.assertEqual(max_integer([7]), 7)
        # Test with an empty list.
        self.assertEqual(max_integer([]), None)
        # Test with a list of floats.
        self.assertEqual(max_integer([1.1, 2.2, 3.3]), 3.3)
        # Test with a list of integers and floats.
        self.assertEqual(max_integer([1, 2.2, 3]), 3)
        # Test with a list containing a single negative float.
        self.assertEqual(max_integer([-2.5]), -2.5)

    def test_max_integer_errors(self):
        # Test with a non-list argument.
        with self.assertRaises(TypeError):
            max_integer(123)

        # Test with a list containing non-numeric types.
        with self.assertRaises(TypeError):
            max_integer([1, 2, "three"])

if __name__ == '__main__':
    unittest.main()