import unittest
from student import Student

class TestStudent(unittest.TestCase):

    def test_full_name(self):
        student = Student("Test", "Student")

        self.assertEqual(student.full_name, 'Test Student')

    def test_alert_santa(self):
        student = Student("Test", "Santa")
        student.alert_santa()

        self.assertTrue(student.naughty_list)


if __name__ == "__main__":
    unittest.main()
