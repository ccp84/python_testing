import unittest
from evens import even_number_of_evens


class TestEvens(unittest.TestCase):

    def test_throws_error_if_value_is_not_list(self):
        self.assertRaises(TypeError, even_number_of_evens, 4)
    
    def test_values_passed_in(self):
        self.assertEqual(even_number_of_evens([]), False)
        self.assertEqual(even_number_of_evens([2, 4]), True)
        self.assertEqual(even_number_of_evens([2]), False)
        self.assertEqual(even_number_of_evens([3]), False)
        self.assertEqual(even_number_of_evens([3, 5]), False)
        self.assertEqual(even_number_of_evens([3, 4]), False)


if __name__ == "__main__":
    unittest.main()
