import unittest
from evens import even_number_of_evens


class TestEvens(unittest.TestCase):

    def test_function_returns_true(self):
        self.assertTrue(even_number_of_evens([]))


if __name__ == "__main__":
    unittest.main()
